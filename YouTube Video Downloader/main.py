from pytube import YouTube
from pytube.exceptions import AgeRestrictedError


def Download_file(url, quality='highest'):
    tk_link = YouTube(url)
    tk_link = tk_link.streams.get_by_resolution(quality)

    #  **** Imp Note ****
    # In the above line 6 and line 7, URL of the video plus the resolution of that video
    # would be stored in the same variable name, if not so, the code will still run but, the
    # file will not be stored on the local storage.

    try:
        print(f"Downloading the video file having the title --> {tk_link.title}")
        tk_link.download()
        print("Download complete!")

        if tk_link.captions:

            if 'en' in tk_link.captions:
                print("Downloading the captions")
                subtitle = tk_link.captions['en']
                subtitle.download(title=tk_link.title)
                print("Captions download complete!")

            else:
                print("English captions are not available.")

    except AttributeError:
        print(f"Error: Stream with resolution '{quality}' not found.")

    except AgeRestrictedError:
        print("Age restricted video, unable to download. Please sign in to YouTube.")

    except Exception as e:
        print(f"Error: {str(e)}")


def repeat_bro():
    video_url = input("Enter the YouTube video URL: ")
    video_quality = input("Enter the desired video quality (e.g., 720p, 480p, or highest): ")
    Download_file(video_url, video_quality)


def main_function():
    while 1:
        print("\nWelcome to Youtube Video Downloader")
        print("   Developed by Talha Khalid")
        print("\n")

        repeat_bro()

        option = str(input("\nDo you want to try it again ? If yes 'Press y' otherwise press any key to exit = "))

        if option.lower() != 'y':
            break

    print("Thanks for using my software/application. Have a lovely day :)")


main_function()

