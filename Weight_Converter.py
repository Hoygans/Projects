import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("500x300")
app.title("Colin's Weight Converter.py")


def button_callback():
    weight = float(entry_1.get())
    entry_1.delete(0, 20)
    unit = combobox_1.get()
    conversion = combobox_2.get()

    if unit == "Kilograms" and conversion == "Pounds":
        answer1 = weight * 2.20462
        answer = round(answer1, 3)
        entry_1.insert(0, F"{answer} Pounds")
    if unit == "Pounds" and conversion == "Kilograms":
        answer1 = weight * 0.453592
        answer = round(answer1, 3)
        entry_1.insert(0, F"{answer} Kilograms")
    if unit == "Grams" and conversion == "Pounds":
        answer1 = weight * .00220462
        answer = round(answer1, 3)
        entry_1.insert(0, F"{answer} Pounds")
    if unit == "Kilograms" and conversion == "Grams":
        answer1 = weight * 1000
        answer = round(answer1, 3)
        entry_1.insert(0, F"{answer} Grams")
    if unit == "Pounds" and conversion == "Grams":
        answer1 = weight * 453.592
        answer = round(answer1, 3)
        entry_1.insert(0, F"{answer} Grams")
    if unit == "Grams" and conversion == "Kilograms":
        answer1 = weight * .001
        answer = round(answer1, 3)
        entry_1.insert(0, F"{answer} Kilograms")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text="Weight Converter",
font= ("Impact", 30), text_color= "#6cc0e5")
label_1.pack(pady=10, padx=10)

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Kilograms", "Grams", "Pounds"], width=175, button_color="#6cc0e5")
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Unit of Measurement")

combobox_2 = customtkinter.CTkComboBox(frame_1, values=["Kilograms", "Grams", "Pounds"], width=175,button_color= "#6cc0e5")
combobox_2.pack(pady=10, padx=10)
combobox_2.set("To unit of Measurement")

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter the weight that you want converted", width=300)
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Convert", corner_radius=20, fg_color="#6cc0e5")
button_1.pack(pady=10, padx=10)

app.mainloop()