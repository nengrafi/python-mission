from services.exception import input_number
from services.QuizGame import QuizGame
from services.save import load

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

quiz_num = 0
quiz = {}
max_score = 0

def quiz_solve():
    global quiz_num,quiz,max_score
    if quiz_num <= 0:
        print("퀴즈가 존재하지 않습니다\n")
        return

    num = 0
    ans = 0

    print(f"퀴즈를 시작합니다 (총 {quiz_num}문제)")

    while num != quiz_num:
        num += 1
        print(f"[문제 {num}]\n")
        print(f"{quiz[num]['question']}\n")
        player_input = input("정답 입력: ").strip()
        if quiz[num]['answer'] == player_input:
            print("정답입니다!!!!\n")
            ans += 1
        else:
            print("오답입니다.....\n")

    print(f"{quiz_num}문제 중에서 {ans}문제 정답!\n")
    print(f"총 점수는 {100*ans/quiz_num}입니다!!!\n")
    if max_score < 100*ans/quiz_num:
        max_score = 100*ans/quiz_num
        print("축하드립니다!!! 신기록입니다!!!\n")

while True:
    print(menu)
    data = load()
    quizgame = QuizGame(data)
    player_num = input_number("번호를 입력하세요: ",1,5)
    if player_num == 5:
        break
    elif player_num == 1:
        quizgame.quiz_solve()
    elif player_num == 2:
        quizgame.quiz_add()
    elif player_num == 3:
        quizgame.quiz_list()
    elif player_num == 4:
        quizgame.quiz_score()
