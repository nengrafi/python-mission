from services.exception import input_number,input_str
class Quiz:
    def __init__(self,question:str, choices: list, answer: int,hint:str):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def display(self):
        print(self.question + "\n")

        for i,choice in enumerate(self.choices, start = 1):
            print(f"{i}. {choice}\n")
        
    def Correct(self):
        player_answer = input_number("정답을 입력하세요 (1~4): ",1,4)

        if player_answer == self.answer:
            print("\n정답입니다!\n")
            return True

        print("\n오답입니다!\n")
        return False
         
    def Hint(self,score):
        hint = input_number("힌트를 원하시면 1번을 원하지 않으시면 0번을 눌러주세요. (힌트 제공시 점수가 차감됩니다): ",0,1)
        if hint == 1:
            if score >= 0:
                score -= 0.5
            print("\n" + self.hint + "\n")

        return score
