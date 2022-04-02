from pytube import YouTube
from colorama import init, Fore


def on_complete(stream, filepath):
    print('Download complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_string)

init()
link = input('YouTube link: ')
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# information
print(Fore.BLUE + f'Title:   \033[39m {video_object.title}')
print(Fore.BLUE + f'Minutes: \033[39m {round(video_object.length // 60)} minutes {round(video_object.length % 60,2)} seconds')
print(Fore.BLUE + f'Views:   \033[39m {video_object.views}')
print(Fore.BLUE + f'Author:  \033[39m {video_object.author}')

# Download 
print(Fore.BLUE + 'download:' + 
Fore.GREEN + '(b)est \033[39m | ' +
Fore.RED + '(w)orst \033[39m | ' +
Fore.YELLOW + '(a)udio \033[39m | ' +
Fore.CYAN +  '(e)xit \033[39m')
download_choice = input('choice: ')

match download_choice:
    case 'b':
        video_object.streams.get_highest_resolution().download()
    case 'w':
        video_object.streams.get_lowest_resolution().download()
    case 'a':
        video_object.streams.get_audio_only().download()