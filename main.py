from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for question in question_data:
    questions.append(Question(question["question"], question["correct_answer"]))

brain = QuizBrain(questions)

while brain.has_more_questions():
    brain.next_question()

print(f"\n\nQuiz is over, your final score is: {brain.score}")