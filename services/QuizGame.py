from services.save import save,load
from services.exception import input_str,input_number
from models.quiz import Quiz
class QuizGame:
    def __init__(self,data:dict):
        self.data = data

    def quiz_add(self):
        print("새로운 퀴즈를 추가합니다! \n")
        text = ""
        player_question = input_str("문제를 입력하세요: ")
        text += player_question + "\n"
        choice_list = []
        for i in range(4):
            player_question = input_str(f"선택지 {i+1}: ")
            choice_list.append(player_question)
        player_question = input_number("정답 번호 (1~4): ",1,4)
        self.data["quiz"].append(
            {
                "question" : text,
                "choices" : choice_list,
                "answer" : player_question
            }
        )
        save(self.data)

    def quiz_list(self):
        quiz_num = len(self.data["quiz"])
        print(f"등록된 퀴즈 목록 (총 {quiz_num}개)\n")
        for i,quiz in enumerate(self.data["quiz"],start=1):
            question = quiz["question"]
            print(i + ". " + question + "\n")

    def quiz_score(self):
        print(f"최고 점수: {self.data["max_score"]}")       

    def quiz_solve(self):
        max_score = self.data["max_score"]
        score = 0

        for item in self.data["quiz"]:
            quiz = Quiz(item["question"],item["choices"],item["answer"])
            quiz.display()
            correct = quiz.Correct()
            if correct : score += 1

        if max_score < score * 100 / len(self.data["quiz"]):
            self.data["max_score"] = score * 100 / len(self.data["quiz"])