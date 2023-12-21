import customtkinter
import random

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("780x400")
app.title("Colin's Computer Quiz.py")
score = 0
def button_callback():

    answer = entry_2.get()
    if answer.lower() in correct_answer:
        answer_correct()
    else:
        entry_3.delete(0,100)
        entry_3.insert(0, "Wrong")
        random_question = random.choice(next_question)
        entry_1.delete(0, 100)
        entry_2.delete(0, 100)
        entry_1.insert(0, random_question)
        next_question.remove(random_question)
def answer_correct():
    global score
    global next_question
    score += 1
    question_length = len(next_question)
    entry_1.delete(0, 100)
    entry_2.delete(0, 100)
    entry_3.delete(0, 50)
    entry_3.insert(0, score)

    if question_length > 0:
        random_question = random.choice(next_question)
        entry_1.insert(0, random_question)
        next_question.remove(random_question)

    if question_length == 0:
        entry_1.insert(0, "Congratulations on completing the quiz!")
        entry_2.insert(0, F"You got {score} out of 9!")


correct_answer = ["central processing unit", "graphics processing unit", "power supply", "application programming interface", "bitcoin", "dots per inch", "hard disk drive", "solid state drive", "liquid crystal display"]
next_question = ["What does CPU stand for?", "What does GPU stand for?", "What does PSU stand for?", "What does API stand for?", "What does BTC stand for?",
"What does DPI stand for?", "What does HDD stand for?", "What does SSD stand for?", "What does LCD stand for?"]

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text="Welcome to a computer quiz!")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Quiz Question", width=500)
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Your answer", width=500)
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Score")
entry_3.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text= "SUBMIT")
button_1.pack(pady=10, padx=10)

random_question = random.choice(next_question)
entry_1.insert(0, random_question)
next_question.remove(random_question)

app.mainloop()
