from pytube import YouTube
from tqdm import tqdm


def cli():
    """
    Command Line Interface for downloading YouTube videos.
    """

    def download_video(url):
        """
        Download a video from a given YouTube URL with a progress bar using tqdm.

        Args:
            url (str): The URL of the YouTube video to be downloaded.
        """

        try:
            yt = YouTube(url)

        except:
            exit("\nThe URL you provided is either empty or invalid.")

        stream = yt.streams.get_highest_resolution()
        pbar = tqdm(total=stream.filesize, unit="B", unit_scale=True, colour="red")

        def on_progress(stream, chunk, bytes_remaining):
            """
            Callback function to update the progress bar.

            Args:
                stream (pytube.Stream): The stream being downloaded.
                chunk (bytes): The chunk of data being downloaded.
                bytes_remaining (int): The number of bytes remaining to download.
            """

            pbar.update(len(chunk))

        yt.register_on_progress_callback(on_progress)
        stream.download("downloads/")

        pbar.close()
        print("Download successfully completed!\n")

    video_url = input("\nEnter the URL of the YouTube video: ")
    download_video(video_url)


while True:
    choice = input(
        "Welcome to YouTube Downloader!\n"
        "- Enter 'launch' for Command Line Interface\n"
        "- Enter 'exit' to Exit\n"
        "Enter your input: "
    )

    if choice == "launch":
        cli()

    elif choice.lower() == "exit":
        print("\nThank you for using Youtube Downloader. See you soon!")
        exit()

    else:
        print(f"The choice '{choice}' is not among the available options. Please try again...\n")
