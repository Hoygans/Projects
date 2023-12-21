from AyDictionary import AyDictionary
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("540x780")
app.title("Colin's Dictionary.py")
dict = AyDictionary()


def button_callback(event= None):
    if var.get() == 1:
        dictionary()
    if var.get() == 2:
        synonymns()
    if var.get() == 3:
        antonym()



def dictionary():
    text_1.delete(0.0, 1000.0)
    word = entry_1.get()
    output = dict.meaning(word, 10)
    text_1.insert(0.0, output)


def synonymns():
    text_1.delete(0.0,1000.0)
    word = entry_1.get()
    output = dict.synonym(word, 10)
    text_1.insert(0.0, output)

def antonym():
    text_1.delete(0.0, 1000.0)
    word = entry_1.get()
    output = dict.antonym(word, 10)
    text_1.insert(0.0, output)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

var = customtkinter.IntVar(app)
var.set(1)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text="Dictionary")
label_1.grid(row=0, column=1, pady=10)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value=1, text= "Dictionary")
radiobutton_1.grid(row=1, column=0, pady=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value=2, text= "Synonyms")
radiobutton_2.grid(row=1, column=1, pady=10)

radiobutton_3 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value=3, text= "Antonyms")
radiobutton_3.grid(row=1, column=2, pady=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, width=300)
entry_1.grid(row=2, column=0, columnspan=3, pady=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text= "Find")
button_1.grid(row=3, column=1, pady=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=500, height=480)
text_1.grid(row=4, column=0, columnspan=3, pady=10)

app.bind('<Return>', button_callback)

app.mainloop()