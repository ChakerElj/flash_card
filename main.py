from tkinter import *
from random import *
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
# --------- read the csv file --------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

# ------------- remove word and create word_to_learn.csv file --------------------------------
def is_known():
    word_dict.remove(current_card)
    data = pd.DataFrame(word_dict)
    data.to_csv("data/words to learn.csv", index=False)
    next_card()
    print(len(word_dict))
# -------------- create new flash card function ------

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    french_word = current_card['French']
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(background,image=card_front_back)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():

    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=card_flip_back)

#  ------------- Create the window -------------------
window = Tk()
window.title("Flashy")
window.resizable(False, False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


# -----------------Insert the canvas ---------------
canvas = Canvas(height=526, width=800)
card_front_back = PhotoImage(file="images/card_front.png")
background = canvas.create_image(400, 263, image=card_front_back)
card_flip_back = PhotoImage(file="images/card_back.png")
title = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# -------------- Create the buttons ---------------------
unknown_button_img = PhotoImage(file="images/wrong.png")
known_button_img = PhotoImage(file="images/right.png")
unknown_button = Button(image=unknown_button_img, command=next_card, highlightthickness=0)
known_button = Button(image=known_button_img, command=is_known, highlightthickness=0)
unknown_button.grid(row=1, column=0)
known_button.grid(row=1, column=1)
next_card()
window.mainloop()
