import requests
import html
from tkinter import *

parameters = {"amount": 10,
              "category": 12,
              "difficulty":"medium",
              "type": "boolean"}

question_bank = []
what_is_clicked = ''
SCORE = 0
BACKGROUND_COLOR = "#0d335d"
ques_num = 0
current_question = ''
current_answer = ''


def get_question_from_api():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = [html.unescape(question_text), question_answer]
        question_bank.append(new_question)


def true_pressed():
    check_answer("True")

def false_pressed():
    check_answer("False")

def next_question():
    global ques_num,current_question,current_answer, quiz_message
    print(ques_num)
    current_question = question_bank[ques_num][0]
    current_answer = question_bank[ques_num][-1]
    canvas.itemconfig(quiz_text, text = f'{current_question}')

def check_answer(useranswer):
    global current_question,current_answer,ques_num, quiz_message, SCORE, response
    if useranswer == current_answer:
        canvas.config(bg = 'green')
        window.config(bg='green')
        ques_num +=1
        SCORE +=1
        canvas.itemconfig(quiz_score, text = f'Score: {SCORE}')
        flip_back = window.after(1500, func=next_question)
        flip = window.after(1500, func=default)

    elif useranswer!= current_answer:
        canvas.config(bg='red')
        window.config(bg='red')
        ques_num += 1
        flip_back = window.after(1500, func=next_question)
        flip = window.after(1500, func=default)

    elif ques_num > len(question_bank):
        false_button.config(state="disabled")
        true_button.config(state="disabled")
        canvas.create_text(250, 207, width=250, text=f"Quiz Over! Final Score: {SCORE}", font=("Arial", 25, "bold"),
                           fill="white")


def default():
    global response
    canvas.config(bg=BACKGROUND_COLOR)
    window.config(bg=BACKGROUND_COLOR)



###-----UI CREATION----
window = Tk()
window.title("Quizzler")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

canvas = Canvas(width=500, height=414, bg = BACKGROUND_COLOR, highlightthickness=0)
background_img = PhotoImage(file="images/quiznight.png")
canvas.create_image(250, 220, image=background_img)
quiz_text = canvas.create_text(250, 207, width=250, text = "hello",font=("Arial", 25, "bold"), fill="white")
quiz_score = canvas.create_text(400, 10, width=90, text = f"Score: {SCORE}",font=("Arial", 15, "bold"), fill="white")
quiz_response = canvas.create_text(250, 7, width=200,font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=1, column=1,columnspan =3)

true_img = PhotoImage(file="images/true.png")
true_button = Button(image=true_img, highlightthickness=0, command = true_pressed)
true_button.grid(row=2, column=1)




false_img = PhotoImage(file="images/false.png")
false_button = Button(image=false_img, highlightthickness=0,command = false_pressed)
false_button.grid(row=2, column=3)

get_question_from_api()
next_question()

window.mainloop()



