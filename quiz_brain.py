class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        questao = self.question_list[self.question_number]
        self.question_number += 1
        resp = input(f"Q.{self.question_number}: {questao.text} (True/False)?\n")

        self.checkQuestion(questao.answer,resp)

    def has_more_questions(self):
        return self.question_number < len(self.question_list)

    def checkQuestion(self, correct, answer):
        if correct.lower() == answer.lower():
            print("Good job, it's correct!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The answer is {correct}\n")

        print(f"Your current score is: {self.score}/{self.question_number}\n")
