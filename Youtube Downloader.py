from pytube import YouTube
from pytube.cli import on_progress

link = input('Digite a url do vídeo que deseja baixar: ')

yt = YouTube(link, on_progress_callback = on_progress)
#yt = yt.get_highest_resolution('mp4', '720p')

print("Titulo = ", yt.title)
print("Baixando...")

ys = yt.streams.get_highest_resolution()

ys.download()