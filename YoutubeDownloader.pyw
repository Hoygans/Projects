import customtkinter
from pytube import YouTube
import webbrowser


def startDownload():
    try:
        video = entry1.get()
        progress1.set(0)
        label1.configure(text="Download Started!")
        label1.update()
        YouTube(video, on_progress_callback=on_progress, on_complete_callback=complete, use_oauth=True, allow_oauth_cache=True).streams.filter(
            file_extension='mp4').get_highest_resolution().download()
    except:
        label1.configure(text="Download Error", bg_color="red")
        label1.update()

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_complete = bytes_downloaded / total_size * 100
    percent = (int(percentage_complete))
    label1.configure(text=str(percent) + "%")
    label1.update()
    progress1.set(percent / 95)


def complete(stream, file_path):
    label1.configure(text="Download Complete!", bg_color="green")
    label1.update()
    print(file_path)
    file1 = file_path.replace("\\", "\n")
    label2.configure(text=str(f"File Path:\n{file1}"))
    label2.update()
    webbrowser.open(file_path)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Colin's YouTube Downloader")

label1 = customtkinter.CTkLabel(master=app, text="Please input a URL")
label1.pack(padx=10,pady=10)

entry1 = customtkinter.CTkEntry(master=app, width=380)
entry1.pack(padx=10, pady=10)

progress1 = customtkinter.CTkProgressBar(master=app, width=380)
progress1.set(0)
progress1.pack(padx=10, pady=20)

button1 = customtkinter.CTkButton(master=app, text="Download", command=startDownload)
button1.pack(padx=10, pady=10)

label2 = customtkinter.CTkLabel(master=app, text="")
label2.pack(padx=10, pady=10)

app.mainloop()
