from services.exception import input_str,input_number
from models.quiz import Quiz
from services.save import save,load
import random
class QuizGame:
    def __init__(self,data:dict):
        self.data = data

    def print_menu(self):
        menu = """
==================================================================
퀴즈 게임
==================================================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
==================================================================
"""
        print(menu)

    def quiz_add(self):
        print("\n새로운 퀴즈를 추가합니다! \n")

        question = input_str("문제를 입력하세요: ")
        choices = []
        for i in range(4):
            choice = input_str(f"{i+1}. ")
            choices.append(choice)
        
        answer = input_number("정답을 입력하세요: ",1,4)
        self.data["quiz"].append(
            {
                "question" : question,
                "choices" : choices,
                "answer" : answer
            }
        )
        save(self.data)

    def quiz_list(self):
        if not self.data["quiz"]:
            print("\n등록된 퀴즈가 없습니다.")
            return
        
        quiz_num = len(self.data["quiz"])
        print(f"등록된 퀴즈 목록 (총 {quiz_num}개)\n")
        for i,quiz in enumerate(self.data["quiz"],start=1):
            question = quiz["question"]
            print(str(i) + ". " + question + "\n")

    def quiz_score(self):
        print(f"최고 점수: {self.data['max_score']}")       

    def quiz_solve(self):
        score = 0

        quiz_list = self.data["quiz"].copy()
        random.shuffle(quiz_list)

        quiz_num = input_number("해결할 퀴즈 수를 입력하세요: ",1,len(quiz_list))
        num = 0

        for item in quiz_list:
            if num == quiz_num:
                break
            num += 1
            quiz = Quiz(item["question"],item["choices"],item["answer"])
            quiz.display()
            correct = quiz.Correct()
            if correct : score += 1

        total_score = int(score * 100 / quiz_num)

        print(f"{quiz_num}개중에서 {score}개 정답으로 현재 점수는 {total_score}입니다.\n")


        if self.data["max_score"] == None:
            self.data["max_score"] = total_score

        elif self.data["max_score"] < total_score:
            self.data["max_score"] = total_score
            print("축하합니다! 신기록입니다!\n")

 
