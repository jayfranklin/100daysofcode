
class QuizBrain:
    def __init__(self, question_list, total_score=0, question_number=0):
        self.question_list = question_list
        self.total_score = total_score
        self.question_number = question_number

    def more_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        #print(current_question.text)
        #print(current_question.answer)
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.total_score += 1
        else:
            print("Sorry, that's incorrect.")
        print(f"Correct answer: {correct_answer}")
        print(f"You're current score is {self.total_score}/{self.question_number}\n")

    def final_score(self):
        print("You've completed the quiz!")
        print(f"You're final score was {self.total_score}/{len(self.question_list)}")




