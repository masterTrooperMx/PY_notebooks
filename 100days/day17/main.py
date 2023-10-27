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
        guess = input("True or False?: ")
        if(bool(guess)):
            if quiz_brain.check_answer_number(guess):
                print("Right answer!")
            else:
                print("Wrong answer, sorry!")
            quiz_brain.print_score()
        else:
            print("input is not recognized, please just True or False")
    else:
        print("OK bye!")