from pytube import YouTube
from colorama import Fore,Style

def completado(stream, file_path):
    print(f'{Fore.GREEN}Termino la descarga el archivo esta en {file_path}{Style.RESET_ALL}')

def progreso(stream, chunk, bytes_remaining):
    print(f'\n{Fore.BLUE}{round(100 - (bytes_remaining / stream.filesize * 100))} %{Style.RESET_ALL}')

def muestra_info():
    print(f'\n\t{Fore.LIGHTYELLOW_EX}titulo: {objeto_video.title}{Style.RESET_ALL}')
    print(f'\t{Fore.LIGHTYELLOW_EX}duración: {round(objeto_video.length / 60,2)} minutos{Style.RESET_ALL}')
    print(f'\t{Fore.LIGHTYELLOW_EX}autor: {objeto_video.author}{Style.RESET_ALL}')

# variables
link = input(f'{Fore.LIGHTMAGENTA_EX}YouTube Link: {Style.RESET_ALL}')
objeto_video = YouTube(link, on_complete_callback = completado, on_progress_callback = progreso)
calidad_video = input(f'{Fore.BLUE}Selecciona la resolucion a descargar --> alta, baja, audio: {Style.RESET_ALL}').lower()

# descarga de videos
muestra_info()
if calidad_video == 'alta': 
    objeto_video.streams.get_highest_resolution().download(r'C:\Users\quentin\Videos')
elif calidad_video == 'baja':
    objeto_video.streams.get_lowest_resolution().download(r'C:\Users\quentin\Videos')
elif calidad_video == 'audio':
    objeto_video.streams.get_audio_only().download(r'C:\Users\quentin\Music')
else: 
    print(f'{Fore.LIGHTRED_EX}\nLa opción no es válida!!!{Style.RESET_ALL}')
    quit() 