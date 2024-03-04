import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = []

try:
    data = pandas.read_csv("/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = "/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/data/french_words.csv"
    data = pandas.read_csv(original_data)

to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    global to_learn
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/data/words_to_learn.csv", index=False)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/images/card_front.png")
card_back =  PhotoImage(file="/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

image_unknown = PhotoImage(file="/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/images/wrong.png")
unknown_button = Button(image=image_unknown, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

image_known = PhotoImage(file="/python 100 days bootcamp/Github.git/Day - 31 Flash card pj/images/right.png")
known_button = Button(image=image_known, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
