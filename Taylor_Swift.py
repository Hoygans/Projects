import random
import customtkinter


songs = ("The 1",
"Afterglow",
"The Alcott",
"All of the Girls You Loved Before",
"All Too Well",
"All You Had to Do Was Stay",
"American Girl",
"Anti-Hero",
"The Archer",
"August",
"Babe",
"Baby",
"Back to December",
"Bad Blood",
"Beautiful Eyes",
"Beautiful Ghosts",
"Begin Again",
"Bejeweled",
"The Best Day",
"Best Days of Your Life",
"Bette Davis Eyes",
"Better Man",
"Better than Revenge",
"Betty",
"Bigger Than the Whole Sky",
"Big Star (Live)",
"Birch",
"Blank Space",
"Both of Us",
"Breathe",
"Breathless",
"Bye Bye Baby",
"Call It What You Want",
"Cardigan",
"Carolina",
"Champagne Problems",
"Change",
"Christmas Must Be Something More",
"Christmas Tree Farm",
"Christmases When You Were Mine",
"Clean",
"Closure",
"Cold as You",
"Come Back... Be Here",
"Come in with the Rain",
"Coney Island",
"Cornelia Street",
"Cowboy like Me",
"Cruel Summer",
"Dancing with Our Hands Tied",
"Daylight",
"Death by a Thousand Cuts",
"Dear John",
"Dear Reader",
"Delicate",
"Don't Blame Me",
"Don't You",
"Dorothea",
"Dress",
"Drops of Jupiter",
"Enchanted",
"End Game",
"Epiphany",
"Evermore",
"Everything Has Changed",
"Exile",
"Eyes Open",
"False God",
"Fearless",
"Fifteen",
"Forever & Always",
"Forever Winter",
"Gasoline",
"Getaway Car",
"Girl at Home",
"Glitch",
"Gold Rush",
"Gorgeous",
"The Great War",
"Half of My Heart",
"Happiness",
"Haunted",
"Hey Stephen",
"High Infidelity",
"Highway Don't Care",
"Hits Different",
"Hoax",
"Hold On",
"Holy Ground",
"How You Get the Girl",
"I Almost Do",
"I Bet You Think About Me",
"I Did Something Bad",
"I Don't Wanna Live Forever",
"I Forgot That You Existed",
"I Heart ?",
"I Knew You Were Trouble",
"I Know Places",
"I Think He Knows",
"I Want You Back",
"I Wish You Would",
"If This Was a Movie",
"Illicit Affairs",
"Innocent",
"Invisible",
"Invisible String",
"It's Nice to Have a Friend",
"It's Time to Go",
"I'm Only Me When I'm with You",
"Ivy",
"Jump Then Fall",
"The Joker and the Queen",
"Karma",
"King of My Heart",
"Labyrinth",
"The Lakes",
"Last Christmas",
"The Last Great American Dynasty",
"Last Kiss",
"The Last Time",
"Lavender Haze",
"Long Live",
"Long Live",
"Long Story Short",
"London Boy",
"Look What You Made Me Do",
"Love Story",
"Lover",
"Lover (Remix)",
"The Lucky One",
"Macavity",
"Mad Woman",
"The Man",
"Marjorie",
"Maroon",
"Mastermind",
"Mary's Song (Oh My My My)",
"Me!",
"Mean",
"Message in a Bottle",
"Midnight Rain",
"Mine",
"Mirrorball",
"Miss Americana & the Heartbreak Prince",
"The Moment I Knew",
"Mr. Perfectly Fine",
"My Tears Ricochet",
"Never Grow Up",
"New Romantics",
"New Year's Day",
"No Body, No Crime",
"Nothing New",
"Only the Young",
"The Other Side of the Door",
"Our Song",
"Ours",
"Out of the Woods",
"The Outside",
"Paper Rings",
"Paris",
"Peace",
"A Perfectly Good Heart",
"Picture to Burn",
"A Place in This World"	,
"Question...?",
"...Ready for It?",
"Red",
"Renegade",
"Right Where You Left Me",
"Ronan",
"Run",
"Sad Beautiful Tragic",
"Safe & Sound",
"Santa Baby",
"September",
"Seven",
"Shake It Off",
"Should've Said No",
"Silent Night",
"Snow on the Beach",
"So It Goes...",
"Soon You'll Get Better",
"Sparks Fly",
"Speak Now",
"Starlight",
"State of Grace",
"Stay Beautiful",
"Stay Stay Stay",
"The Story of Us",
"Style",
"Superman",
"Superstar",
"Sweet Nothing",
"Sweeter than Fiction",
"Teardrops on My Guitar",
"Tell Me Why",
"That's When",
"This Is Me Trying",
"This is What You Came For",
"This Is Why We Can't Have Nice Things",
"This Love",
"Tied Together with a Smile",
"Tim McGraw",
"'Tis the Damn Season",
"Today Was a Fairytale",
"Tolerate It",
"Treacherous",
"Two Is Better Than One",
"Umbrella",
"Untouchable",
"The Very First Night",
"Vigilante Shit",
"The Way I Loved You",
"We Are Never Ever Getting Back Together",
"Welcome to New York",
"We Were Happy",
"White Christmas",
"White Horse",
"Wildest Dreams",
"Willow",
"Wonderland",
"Would've, Could've, Should've",
"You All Over Me",
"You Are in Love",
"You Belong with Me",
"You'll Always Find Your Way Back Home",
"You're on Your Own, Kid",
"You Need to Calm Down",
"You're Not Sorry")

print(len(songs))
def button_callback():
    random_num = random.randint(0, 228)
    new_song = (songs[random_num])
    e.delete(0,100)
    e.insert(0, new_song)
    text_1.insert(0.0,  new_song + "/n")

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x550")
app.title("Swifty Song Selector")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

e = entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Song", width=300)
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1,
command=button_callback, text= "New Song")
button_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=300, height=400)
text_1.pack(pady=10, padx=10)


app.mainloop()
