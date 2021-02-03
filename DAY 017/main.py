from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

questions = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_q = Question(text, answer)
    questions.append(new_q)

quiz = QuizBrain(questions)

while quiz.more_questions():
    quiz.next_question()

quiz.final_score()
