"""Goals for V3: Add threading to stop app freezing between progress updates. Improve error handling.
Remove global file_browser. Remove redunant file_check. Addvuser choice of file type and quality. 
Add new color scheme, or add user definable color schemes."""
import customtkinter
from pytube import YouTube
import webbrowser


# If Checkbox is checked, show download location label, *redundant*
def check():
    if file_check.get() == 1:
        label2.configure(text=f"Download location: {file_browser}")
        label2.update()


# Opens the file directory of your computer to select where the file should go. Also updates the download location label
def file_location():
    global file_browser
    file_browser = customtkinter.filedialog.askdirectory()
    if file_check.get() == 1:
        label2.configure(text=f"Download location: {file_browser}")
        label2.update()


""" Gets URL from entry1, resets progress bar, updates label1, and attempts to download the highest quality mp4 
regardless of age restriction. If failed, updates label1 to Download Error. """
def start_download():
    try:
        video = entry.get()
        progress1.set(0)
        label1.configure(text="Download Started!", bg_color="transparent")
        label1.update()
        YouTube(video, on_progress_callback=on_progress,
                on_complete_callback=complete,
                use_oauth=True,
                allow_oauth_cache=True).streams.filter(
            file_extension='mp4').get_highest_resolution().download(file_browser)
    except:
        label1.configure(text="Download Error", bg_color="red")
        label1.update()
        if len(video) == 0:
            label1.configure(text="Please enter a valid URL", bg_color="red")


# Calculates file size & data downloaded to give a percentage of completion. Updates label1 and progress bar accordingly
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_complete = bytes_downloaded / total_size * 100
    percent = (int(percentage_complete))
    label1.configure(text=str(percent) + "%")
    label1.update()
    progress1.set(percentage_complete / 100)


# Updates label1 to complete and updates label 3 to finished file path. If checkbox2 is checked, plays video.
def complete(stream, file_path):
    label1.configure(text="Download Complete!", bg_color="green")
    label1.update()
    file1 = file_path.replace("/", "\n").replace("\\", "\n")
    label3.configure(text=f"File Path:\n{file1}")
    label3.update()
    if playback.get() == 1:
        webbrowser.open(file_path)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x600")
app.title("Colin's YouTube Downloader")

label1 = customtkinter.CTkLabel(master=app, text="Please input a URL")
label1.pack(padx=10, pady=10)

entry = customtkinter.StringVar()
entry1 = customtkinter.CTkEntry(master=app, width=380, textvariable=entry)
entry1.pack(padx=10, pady=10)

progress1 = customtkinter.CTkProgressBar(master=app, width=380)
progress1.set(0)
progress1.pack(padx=10, pady=20)

label2 = customtkinter.CTkLabel(master=app, text="")
label2.pack(padx=10, pady=10)

button1 = customtkinter.CTkButton(master=app, text="Browse Video File Location", command=file_location)
button1.pack(padx=10, pady=10)

file_check = customtkinter.IntVar()
checkbox1 = customtkinter.CTkCheckBox(master=app, text="Use custom file path", variable=file_check, command=check)
checkbox1.pack(padx=10, pady=10)

playback = customtkinter.IntVar()
checkbox2 = customtkinter.CTkCheckBox(master=app, text="Play video when downloaded", variable=playback)
checkbox2.pack(padx=10, pady=10)

button2 = customtkinter.CTkButton(master=app, text="Download", command=start_download)
button2.pack(padx=10, pady=10)

label3 = customtkinter.CTkLabel(master=app, text="")
label3.pack(padx=10, pady=10)

app.mainloop()
