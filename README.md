## OOP 설계 원칙
- main.py를 통해서 퀴즈를 작동
- models에 data를 가지고 있는 class quiz를 저장하여 데이터를 표현하는 객체 관리
- services에 QuizGame 정의, 예외 처리, 저장과 로그 등의 기능 구현
- data에 사전에 준비한 데이터를 저장
- state.json을 저장소로 사용
- docs에 log및 image를 저장하여 README.md의 가독성 증가

## 진행과정
### 1. github 설정

git remote add origin git@github.com:nengrafi/python-mission.git
git remote -v

origin  git@github.com:nengrafi/python-mission.git (fetch)
origin  git@github.com:nengrafi/python-mission.git (push)

git init
git add .
git commit -m "first"
git push origin main

오브젝트 나열하는 중: 3, 완료.
오브젝트 개수 세는 중: 100% (3/3), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (2/2), 완료.
오브젝트 쓰는 중: 100% (3/3), 222 bytes | 222.00 KiB/s, 완료.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:nengrafi/python-mission.git
 * [new branch]      main -> main

### 2. 메뉴 기능

### 3. 공통 입력/ 예외 처리 기준

### 4. Quiz 클래스

### 5. 기본 퀴즈 데이터

### 6. 퀴즈 풀기
nangrapigood2005@c5r8s3 python-mission % git branch
  main
* test
nangrapigood2005@c5r8s3 python-mission % git switch main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'보다 3개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)
nangrapigood2005@c5r8s3 python-mission % git merge test
업데이트 중 d354bea..c729934
Fast-forward
 .gitignore           |   1 +
 docs/test_quiz_6.png | Bin 0 -> 101253 bytes
 main.py              |   7 ++-----
 models/quiz.py       |   5 +++--
 test.py              |  11 +++++++++++
 5 files changed, 17 insertions(+), 7 deletions(-)
 create mode 100644 docs/test_quiz_6.png
 create mode 100644 test.py
 
### 7. 퀴즈 추가

### 8. 퀴즈 목록

### 9. 점수 확인

### 10. QuizGame class

### 11. 파일 저장/불러오기

### 12. Git 저장소 복제 실습

## 오류

### 1. 지역변수와 전역번수

raceback (most recent call last):
  File "/Users/nangrapigood2005/python-mission/game.py", line 77, in <module>
    quiz_add()
  File "/Users/nangrapigood2005/python-mission/game.py", line 55, in quiz_add
    quiz_num += 1
UnboundLocalError: local variable 'quiz_num' referenced before assignment

-> 함수안에서 += 또는 =을 사용하면 Python은 그 변수를 지역 변수로 판단하기 때문에 값이 없다고 인식하고 오류가 남
-> global <변수이름>을 추가함으로서 그 변수가 전역 변수임을 명시