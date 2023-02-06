import sys
import os
import tkinter
from tkinter import messagebox
import pytube
from pytube.exceptions import RegexMatchError
import PIL


# Function to download the video
def download():
    try:
        # Get the video URL entered by the user
        url_of_video = vid_url_entry.get()
        # Create a YouTube object using the URL
        youtube = pytube.YouTube(url_of_video)
        # Get the first stream that matches the selected resolution
        vid = youtube.streams.filter(res=res_var.get()).first()
        # Download the video to the user's Downloads folder
        vid.download(os.path.expanduser("~/Downloads"))  # The download location may be changed by the user
    except RegexMatchError:
        # Show an error message if the URL is invalid
        messagebox.showwarning("Error", "It cannot be downloaded, please try again.")
    else:
        # Show a message to indicate that the video has been successfully downloaded
        messagebox.showinfo("Done", "Your video has been downloaded and saved in your Downloads folder.")


# Create the root window
root = tkinter.Tk()

# Set the size of the window
root.geometry("400x250")

# Set the title of the window
root.title("YouTube Video Downloader by Alper Celik")


# Create a label to prompt the user to enter the video URL
vid_url_label = tkinter.Label(root, text="Enter video URL: ")
vid_url_label.pack()

# Create an entry widget for the video URL
vid_url_entry = tkinter.Entry(root)
vid_url_entry.pack()

# Create a label to prompt the user to select the video resolution
res_label = tkinter.Label(root, text="Select resolution: ")
res_label.pack()

# Create a variable to store the selected resolution
res_var = tkinter.StringVar()
# Set the default resolution to 360p
res_var.set("360p")

# Create a list of resolution options
res_opts = [("144p", "144p"), ("240p", "240p"), ("360p", "360p"), ("480p", "480p"), ("720p", "720p"), ("1080p", "1080p")]

# Create a radiobutton for each resolution option
for res in res_opts:
    tkinter.Radiobutton(root, text=res[0], variable=res_var, value=res[1]).pack()

# Create a button to start the download
download_button = tkinter.Button(root, text="Download", command=download)
download_button.pack()

# Start the main event loop
root.mainloop()



# by Alper Celik
# All necessary comments added thanks to ChatGPT.
