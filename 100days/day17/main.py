from classes.QuestionModel import Question
from classes.QuestionModel import QuizBrain
from classes.data import question_data

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
#question_bank = [
#    Question(q1, a1)
#]
#print(question_bank)
quiz_brain = QuizBrain(question_bank)
q_num = 0
while q_num >= 0:
    num_q = input("what question (1-12) ")
    q_num = int(num_q)
    quiz_brain.set_number(q_num)
    if q_num >= 0:
        print(f"Q.{q_num}.- {quiz_brain.question_number()} (True/False): ")
    else:
        print("OK bye!")