import customtkinter
import random


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x250")
app.title("Colin's Bill Splitter.py")

def button_callback():
    friends_string = entry_1.get()
    global friends_list
    friends_list = friends_string.split(",")
    entry_1.delete(0, 150)
    entry_1.insert(0, "How much was your bill? ")


def button_callback1():
    entry_1.get()
    entry_1.delete(0, 23)
    bill = float(entry_1.get())
    bill_rounded = round(bill, 2)
    split_bill = bill / len(friends_list)
    split_bill_rounded = round(split_bill, 2)
    random_number = random.choice(friends_list)
    winner = random_number
    entry_1.delete(0, 100)
    entry_1.insert(0, f"Your per person price is ${split_bill_rounded} or {winner} can pay the full bill of ${bill_rounded}.")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text="Bill Splitter/Randomizer")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1,width=500 ,placeholder_text="Enter name of each person followed by a comma.")
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Enter list of people")
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, command=button_callback1, text="Enter Bill")
button_2.pack(pady=10, padx=10)

app.mainloop()

