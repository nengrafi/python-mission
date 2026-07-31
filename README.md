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