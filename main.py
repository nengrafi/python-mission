
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

def quiz_add():
    global quiz_num
    print("새로운 퀴즈를 추가합니다! \n")
    text = ""
    player_question = input("문제를 입력하세요: ")
    text += player_question + "\n"
    for i in range(4):
        player_question = input(f"선택지 {i+1}: ")
        text += str(i+1) + ". " +player_question + "\n"
    player_question = input("정답 번호 (1~4): ")
    quiz_num += 1
    quiz[quiz_num] = {
        "question" : text,
        "answer" : player_question
    } 

def quiz_list():
    global quiz_num,quiz
    print(f"등록된 퀴즈 목록 (총 {quiz_num}개)\n")
    for i in range(quiz_num):
        print(f"{i+1}. {quiz[i+1]['question']}\n")

def quiz_score():
    global max_score
    print(f"최고 점수: {max_score}")

while True:
    print(menu)
    player_num = int(input("번호를 입력하세요: "))
    if player_num == 5:
        break
    elif player_num == 1:
        quiz_solve()
    elif player_num == 2:
        quiz_add()
    elif player_num == 3:
        quiz_list()
    elif player_num == 4:
        quiz_score()
    elif player_num == "":
        print("잘못된 입력입니다/\n")
    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.\n")
