from services.exception import input_number
class Quiz:
    def __init__(self,question:str, choices: list, answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer

    def quiz_list(self):
        print(f"등록된 퀴즈 목록 (총 {quiz_num}개)\n")
        for i in range(quiz_num):
            print(f"{i+1}. {quiz[i+1]['question']}\n") 

    def Correct(self,question,answer):
        player_answer = input_number("정답을 입력하세요 (1~4): ",1,4)
        if player_answer = answer
        
