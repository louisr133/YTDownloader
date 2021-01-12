import sys
import concurrent.futures
from pytube import YouTube
import tkinter as tk
from pytube.exceptions import RegexMatchError

window = tk.Tk()
window.geometry("600x200")
window.title('YT Downloader')
window.configure(background='#35363a')

link_var = tk.StringVar()
print("open")


def write_to_loading_lbl(percentage_of_completion=0):
    loading_lbl["text"] = "Loading: {}".format(percentage_of_completion)


def handle_dl():
    print("starting Download")
    link = link_var.get()

    def get_video():
        yt = YouTube(link)
        yt.register_on_progress_callback(on_progress)
        yt.streams.filter(progressive=True).get_highest_resolution().download('/Users/louis/Desktop')
        status_lbl["text"] = "Downloaded: {}".format(yt.title)

    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        print(percentage_of_completion)

    try:
        get_video()
    except RegexMatchError:
        status_lbl["text"] = "Error. Please Enter Valid Link"
    except:
        print("Unexpected error:", sys.exc_info()[0])
        status_lbl["text"] = "System error: {} " .format(sys.exc_info()[0])
        raise


def clear_link():
    link_var.set("")
    status_lbl["text"] = ""


phrase = tk.Label(
    text="Enter the YouTube Link You Wish to Download Below",
    foreground='white',
    background='#35363a',
    width=50,
    height=2,
    highlightbackground='#35363a',
)

link_ent = tk.Entry(
    textvariable=link_var,
    width=50,
    highlightbackground='#35363a',
)
btn_frm = tk.Frame(
    master=window,
    background='#35363a'
)
download_btn = tk.Button(
    master=btn_frm,
    text="Start Download",
    width=25,
    highlightbackground='#35363a',
    command=handle_dl
)
clear_btn = tk.Button(
    master=btn_frm,
    text="Clear Text",
    width=25,
    highlightbackground='#35363a',
    command=clear_link
)

frame2 = tk.Frame(
    master=window,
    background='#35363a'
)
status_lbl = tk.Label(
    text="",
    foreground='white',
    background='#35363a',
    width=50,
    height=2,
    highlightbackground='#35363a',
)
loading_lbl = tk.Label(
        text="Loading",
        foreground='white',
        background='#35363a',
        highlightbackground='#35363a',
    )

phrase.pack()
link_ent.pack()
btn_frm.pack()
download_btn.pack(side=tk.LEFT, padx=5)
clear_btn.pack(side=tk.LEFT, padx=5)
frame2.pack()
status_lbl.pack(fill=tk.X)
loading_lbl.pack()

window.mainloop()
