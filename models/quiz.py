class Quiz:
    def __init__(self,question:str, choices: list, answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer

    def quiz_list():
        print(f"등록된 퀴즈 목록 (총 {quiz_num}개)\n")
        for i in range(quiz_num):
            print(f"{i+1}. {quiz[i+1]['question']}\n") 

    def Correct():
        
