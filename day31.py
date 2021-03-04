from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
# ---------------------------- READ THE DATA AND GENERATE CARDS ------------------------------- #
data = pd.read_csv("data/datanew.csv")
to_learn = data.to_dict(orient="records")

def generate_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    front_canvas.itemconfig(title_text, text="Question", fill ="black")
    front_canvas.itemconfig(word_text, text = current_word["Question"], fill = "black")
    front_canvas.itemconfig(front, image = card_front)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP THE CARD ------------------------------- #
def flip_card():
    front_canvas.itemconfig(title_text, text="Answer", fill="red")
    front_canvas.itemconfig(word_text, text=current_word["Answer"], fill = 'red')
    front_canvas.itemconfig(front, image=card_back)

def is_known():
    to_learn.remove(current_word)
    generate_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady =50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

front_canvas = Canvas(width=800,height=550, bg = BACKGROUND_COLOR, highlightthickness= 0)
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
front= front_canvas.create_image(400,270,image = card_front)
title_text=front_canvas.create_text(400,135, text = "Title", fill = "black", font=("arial", 35,"italic"))
word_text=front_canvas.create_text(400,270, text = "Word", fill = "black", font=("arial", 30,"bold"))
front_canvas.grid(column = 0, row =0, columnspan = 4)

right_button = Button(image = right, highlightthickness=0, command = is_known)
right_button.grid(column =3, row =2)

wrong_button = Button(image = wrong, highlightthickness=0,command = generate_word)
wrong_button.grid(column =0, row =2)

card_back = PhotoImage(file="images/card_back.png")

generate_word()




window.mainloop()


