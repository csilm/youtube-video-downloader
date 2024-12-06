from pytubefix import YouTube

def download_youtube_video():
    # Prompt user for the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Display video title and details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        
        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Specify download location
        print("Downloading...")
        video_stream.download()  # By default, downloads to the current directory
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the downloader
if __name__ == "__main__":
    download_youtube_video()
