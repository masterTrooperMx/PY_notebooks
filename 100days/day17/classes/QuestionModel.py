class Question:
    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, q_list) -> None:
        self.number = 0
        self.question_list = q_list
        self.score = 0
        self.total = 0

    def set_number(self, num):
        self.number = num
    
    def question_number(self):
        question = self.question_list[self.number-1]
        return question.text
    
    def check_answer_number(self, res):
        question = self.question_list[self.number-1]
        check = False
        if question.answer == res:
            check = True
            self.score += 1
        self.total += 1
        return check
    
    def print_score(self):
        print(f"Score: {self.score}/{self.total}")