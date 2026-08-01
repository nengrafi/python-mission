from services.save import save,load
class QuizGame:
    def __init__(self,data:dict):
        self.data = data

    def quiz_add(self):
        print("새로운 퀴즈를 추가합니다! \n")
        text = ""
        player_question = input("문제를 입력하세요: ")
        text += player_question + "\n"
        choice_list = []
        for i in range(4):
            player_question = input(f"선택지 {i+1}: ")
            choice_list.append(player_question)
        player_question = input("정답 번호 (1~4): ")
        self.data["quiz"].append(
            {
                "question" : text,
                "choices" : choice_list,
                "answer" : player_question
            }
        )
        save(self.data)

    
