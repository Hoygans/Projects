import customtkinter as ctk
from pytube import YouTube
import webbrowser
import threading
import os
import PIL


# Opens the file directory of your computer to select where the file should go.
# Also updates the download location label
def file_location():
    file_browser = ctk.filedialog.askdirectory()
    label2.configure(text=f"Download location: {file_browser}",
                     text_color="MediumOrchid1",
                     font=("Bernard MT Condensed", 12))
    return file_browser


""" Resets progress bar, updates label1, and attempts to download mp4 with 
highest or lowest quality, regardless of age restriction. If failed, updates 
label1 to Download Error. Added ability to download only audio """


def download_video(video, file_browser, on_progress, complete):
    try:
        progress1.set(0)
        label1.configure(text="Download Started!", bg_color="#fef3f4")
        get_video = (YouTube(video, on_progress_callback=on_progress,
                     on_complete_callback=complete,
                     use_oauth=True,
                     allow_oauth_cache=True))
        if dropdown_var1.get() == "Video":
            video_streams = get_video.streams.filter(file_extension="mp4",
                                                     progressive=True)
            if dropdown_var2.get() == "Highest Quality":
                selected_stream = video_streams.get_highest_resolution()
            elif dropdown_var2.get() == "Lowest Quality":
                selected_stream = video_streams.get_lowest_resolution()
        elif dropdown_var1.get() == "Audio":
            selected_stream = get_video.streams.get_audio_only()
        selected_stream.download(file_browser)
    except Exception as e:
        if len(video) == 0:
            label1.configure(text="Please enter a valid URL",
                             bg_color="darkred",
                             font=("Bernard MT Condensed", 12))
        else:
            label1.configure(text=f"Download Error: {e}", bg_color="darkred",
                             font=("Bernard MT Condensed", 12))


# Calculates file size & data downloaded to give a percentage of completion.
# Updates label1 and progress bar accordingly
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_complete = bytes_downloaded / total_size * 100
    percent = (int(percentage_complete))
    label1.configure(text=str(percent) + "%")
    progress1.set(percentage_complete / 100)


# Updates label1 to complete and updates label 3 to finished file path.
# If checkbox1 is checked, plays video.
def complete(stream, file_path):
    label1.configure(text="Download Complete!", text_color="black",
                     bg_color="MediumOrchid1",
                     font=("Bernard MT Condensed", 15))
    file1 = os.path.normpath(file_path).replace("\\", "\n")
    label3.configure(text=f"File Path:\n{file1}",
                     font=("Bernard MT Condensed", 12),
                     text_color="MediumOrchid1")
    if playback.get() == 1:
        webbrowser.open(file_path)


# Gets input from entry1 and activates file_location,
# Threading to keep app from freezing.
def start_download():
    open_cmd()
    video = entry.get()
    file_browser = file_location()
    threading.Thread(target=download_video,
                     args=(video, file_browser, on_progress, complete)).start()


# Opens cmd if first_run_indicator.txt is not present.
def open_cmd():
    file = (r"C:\Users\Cjrus\PycharmProjects\pythonProject\.venv"
            r"\first_run_indicator.txt")
    if not os.path.exists(file):
        os.system("start cmd.exe /k")
        open(file, "w")


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x600")
app.title("Colin's YouTube Downloader")


bg = ctk.CTkImage(PIL.Image.open("background.png"), size=(600, 700))

label = ctk.CTkLabel(master=app, image=bg, text="")
label.place(relheight=1, relwidth=1)

label1 = ctk.CTkLabel(master=app, text="Please input YouTube URL",
                      text_color="MediumOrchid1", bg_color="#fef3f4",
                      font=("Bernard MT Condensed", 20))
label1.pack(padx=10, pady=10)

entry = ctk.StringVar()
entry1 = ctk.CTkEntry(master=app, width=400, textvariable=entry,
                      font=("Bernard MT Condensed", 15),
                      text_color="MediumOrchid1")
entry1.pack(padx=10, pady=10)

progress1 = ctk.CTkProgressBar(master=app, width=400,
                               progress_color="MediumOrchid1")
progress1.set(0)
progress1.pack(padx=10, pady=20)

label2 = ctk.CTkLabel(master=app, text="", bg_color="#fef3f4",
                      font=("Bernard MT Condensed", 12))
label2.pack(padx=10, pady=10)

dropdown_var1 = ctk.StringVar()
dropdown1 = ctk.CTkComboBox(master=app, values=["Video", "Audio"],
                            variable=dropdown_var1,
                            button_color="MediumOrchid1",
                            button_hover_color="MediumOrchid3",
                            text_color="MediumOrchid1", width=160,
                            dropdown_text_color="MediumOrchid1",
                            font=("Bernard MT Condensed", 12),
                            dropdown_font=("Bernard MT Condensed", 12))
dropdown1.set("Choose Video or Audio")
dropdown1.pack(padx=10, pady=10)

dropdown_var2 = ctk.StringVar()
dropdown2 = ctk.CTkComboBox(master=app,
                            values=["Highest Quality", "Lowest Quality"],
                            variable=dropdown_var2,
                            button_color="MediumOrchid1",
                            button_hover_color="MediumOrchid3",
                            text_color="MediumOrchid1", width=160,
                            dropdown_text_color="MediumOrchid1",
                            font=("Bernard MT Condensed", 12),
                            dropdown_font=("Bernard MT Condensed", 12))
dropdown2.set("Choose Quality")
dropdown2.pack(padx=10, pady=10)

playback = ctk.IntVar()
checkbox1 = ctk.CTkCheckBox(master=app, text="Play video when downloaded",
                            variable=playback, fg_color="MediumOrchid1",
                            hover_color="MediumOrchid4", corner_radius=90,
                            text_color="MediumOrchid1", bg_color="#fef3f4",
                            font=("Bernard MT Condensed", 15))
checkbox1.pack(padx=10, pady=10)

button1 = ctk.CTkButton(master=app, text="Download",
                        command=start_download, hover_color="MediumOrchid4",
                        fg_color="MediumOrchid1", text_color="black",
                        font=("Bernard MT Condensed", 20))
button1.pack(padx=10, pady=10)

label3 = ctk.CTkLabel(master=app, text="", bg_color="#fef3f4",
                      font=("Bernard MT Condensed", 12))
label3.pack(padx=10, pady=10)


app.mainloop()
