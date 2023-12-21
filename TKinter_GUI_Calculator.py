import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue") # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("300x350")
app.title("Colin's Calculator")

def button_callback():
    operation = (combobox_1.get())
    a = float(e.get())
    b = float(e2.get())

    if operation == "Addition":
        e3.delete(0, 100)
        answer = a + b
        e3.insert(0, answer)

    if operation == "Subtraction":
        e3.delete(0, 100)
        answer = a - b
        e3.insert(0, answer)

    if operation == "Multiplication":
        e3.delete(0, 100)
        answer = a * b
        e3.insert(0, answer)

    if operation == "Division":
        e3.delete(0, 100)
        answer = a / b
        e3.insert(0, answer)

    if operation == "Operations":
        e3.insert(0, "Pick an operation")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

combobox_1 = customtkinter.CTkComboBox(frame_1,
button_color="blue4", values=["Addition", "Subtraction", "Multiplication", "Division"])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Operations")

e = entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="First Number")
entry_1.pack(pady=10, padx=10)

e2 = entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Second Number")
entry_2.pack(pady=10, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text="=")
label_1.pack(pady=10, padx=10)

e3 = entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Equals")
entry_3.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Calculate", fg_color= "blue4")
button_1.pack(pady=10, padx=10)

app.mainloop()