#Quiz

from question_model_day17 import Question
from data_day17 import question_data
from quiz_brain_day17 import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print("QUIZ!")
while quiz.still_has_questions():
    quiz.next_question()

if quiz.score == len(quiz.question_list):
    reaction = '🙌 You Smart'
else:
    reaction = '🥴 better luck next time'
print("You've completed the quiz, lets find out how you've done...")
print(f'Your final score was {quiz.score}/{len(quiz.question_list)}, {reaction}')




