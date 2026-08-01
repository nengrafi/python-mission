from services.exception import input_number
class Quiz:
    def __init__(self,question:str, choices: list, answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question + "\n")

        for i,choice in enumerate(self.choices, start = 1):
            print(f"{i}. {choice}\n")
        

    def Correct(self):
        player_answer = input_number("정답을 입력하세요 (1~4): ",1,4)

        if player_answer == self.answer:
            print("정답입니다!")
            return True

        print("오답입니다!")
        return False
        
