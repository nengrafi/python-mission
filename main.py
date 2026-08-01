from services.exception import input_number
from services.QuizGame import QuizGame
from services.save import load,save

data = load()
quizgame = QuizGame(data)

try:
    while True:
        quizgame.print_menu()
        player_num = input_number("번호를 입력하세요: ",1,6)
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
        elif player_num == 6:
            quizgame.quiz_delete()

except (KeyboardInterrupt, EOFError):
    print ("프로그램을 안전하게 종료합니다.")
    save(quizgame.data)
