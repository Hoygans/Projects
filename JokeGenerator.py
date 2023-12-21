import random
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x300")
app.title("Colin's Joke Generator")

joke_list = ("I'm afraid for the calendar. \n Its days are numbered.",
"My wife said I should do lunges to stay in shape. \nThat would be a big step forward.",
"Why do fathers take an extra pair of socks when they go golfing? \nIn case they get a hole in one!",
"Singing in the shower is fun until you get soap in your mouth. \nThen it's a soap opera.",
"What do a tick and the Eiffel Tower have in common? \nThey're both Paris sites.",
"What do you call a fish wearing a bowtie? Sofishticated.",
"How do you follow Will Smith in the snow? \nYou follow the fresh prints.",
"If April showers bring May flowers, what do May flowers bring? Pilgrims.",
"I thought the dryer was shrinking my clothes. \nTurns out it was the refrigerator all along.",
"How does dry skin affect you at work? \nYou don’t have any elbow grease to put into it.",
"What do you call a factory that makes okay products? A satisfactory.",
"Dear Math, grow up and solve your own problems.",
"What did the janitor say when he jumped out of the closet? Supplies!",
"Have you heard about the chocolate record player?\n It sounds pretty sweet.",
"What did the ocean say to the beach? \nNothing, it just waved.",
"Why do seagulls fly over the ocean? \nBecause if they flew over the bay, we'd call them bagels.",
"I only know 25 letters of the alphabet. I don't know y.",
"How does the moon cut his hair? Eclipse it.",
"What did one wall say to the other? \nI'll meet you at the corner.",
"What did the zero say to the eight? \nThat belt looks good on you.",
"A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
"Where do fruits go on vacation? Pear-is!",
"I asked my dog what's two minus two. He said nothing.",
"What did Baby Corn say to Mama Corn? Where's Pop Corn?",
"What's the best thing about Switzerland? \nI don't know, but the flag is a big plus.",
"What does a sprinter eat before a race? \nNothing, they fast!",
"Where do you learn to make a banana split? \nSundae school.",
"What has more letters than the alphabet? \nThe post office!",
"Dad, did you get a haircut? No, I got them all cut!",
"What do you call a poor Santa Claus? \nSt. Nickel-less.",
"I got carded at a liquor store, and my Blockbuster card accidentally fell out. \nThe cashier said never mind.",
"Where do boats go when they're sick? \nTo the boat doc.",
"I don't trust those trees. They seem kind of shady.",
"My wife is really mad at the fact that I have no sense of direction. \nSo I packed up my stuff and right!",
"How do you get a squirrel to like you? Act like a nut.",
"Why don't eggs tell jokes? They'd crack each other up.",
"I don't trust stairs. They're always up to something.",
"What do you call someone with no body and no nose? Nobody knows.",
"Did you hear the rumor about butter? Well, I'm not going to spread it!",
"Why couldn't the bicycle stand up by itself? It was two tired.",
"What did one hat say to the other? Stay here! I'm going on ahead.",
"Why did Billy get fired from the banana factory? \nHe kept throwing away the bent ones.",
             )
print(len(joke_list))
def button_callback(event= None):
    text1.delete(0.0, 1000.0)
    new_joke = random.choice(joke_list)
    text1.insert(0.0, new_joke)

frame1 = ctk.CTkFrame(master=app)
frame1.pack(pady=20, padx=60, fill="both", expand=True)

text1 = ctk.CTkTextbox(master=frame1, width=400, height=100)
text1.pack(pady=10, padx=10)

button1 = ctk.CTkButton(master=frame1, command=button_callback, text="Get Joke!")
button1.pack(pady=10, padx=10)

app.bind("<Return>", button_callback)

app.mainloop()