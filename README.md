## 프로젝트 개요
OOP를 이용한 퀴즈 시스템 제작하기

## 퀴즈 주제 선정 이유
인공지능 분야에 흥미가 있어서 이걸 퀴즈로 만들고 싶었다.

## 실행방법
main.py에서 시작하여 진행하면 된다.

## OOP 설계 원칙
- main.py를 통해서 퀴즈를 작동
- models에 data를 가지고 있는 class quiz를 저장하여 데이터를 표현하는 객체 관리
- services에 QuizGame 정의, input 예외 처리, 저장과 로그 등의 기능 구현
- data에 사전에 준비한 데이터를 저장
- state.json을 저장소로 사용
- docs에 log및 image를 저장하여 README.md의 가독성 증가

## 데이터 설계 원칙
- quiz 질문과 max_score을 1차적으로 dict로 저장
- quiz의 key는 list로 넣어서 그 안에 여러 문제들이 들어갈 수 있도록 함
- list 내의 한문제는 dict를 이용해서 question,choices,answer 저장
- choices의 key도 list로 저장하여 4가지 선택지가 저장될 수 있도록 반영

## 진행과정
### 1. github 설정

```bash
$ git remote add origin git@github.com:nengrafi/python-mission.git
$ git remote -v

origin  git@github.com:nengrafi/python-mission.git (fetch)
origin  git@github.com:nengrafi/python-mission.git (push)

$ git init
$ git add .
$ git commit -m "first"
$ git push origin main

오브젝트 나열하는 중: 3, 완료.
오브젝트 개수 세는 중: 100% (3/3), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (2/2), 완료.
오브젝트 쓰는 중: 100% (3/3), 222 bytes | 222.00 KiB/s, 완료.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:nengrafi/python-mission.git
 * [new branch]      main -> main
```
.gitignore의 경우 __pycache__를 설정해서 python 실행시에 나오는 파일들을 무시

### 2. 메뉴 기능

### 3. 퀴즈 풀기
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
 
### 4. 퀴즈 추가

==================================================================
퀴즈 게임
==================================================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
==================================================================

번호를 입력하세요: 2

새로운 퀴즈를 추가합니다! 

문제를 입력하세요: 안녕 테스트 중입니다
1. 정답이에요
2. 아니에요
3. 아님
4. 아님
정답을 입력하세요: 1

==================================================================
퀴즈 게임
==================================================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
==================================================================

번호를 입력하세요: 3
등록된 퀴즈 목록 (총 6개)

1. 다음중 기계학습의 한 종류가 아닌것은?

2. 활성화 함수를 사용하는 가장 큰 이유는?

3. 과적합(Overfitting)을 완화시키기에 가장 적절한 방법은?

4. BERT와 GPT 모델의 가장 큰 차이점으로 적절한 것은?

5. Softmax 함수의 주된 목적은?

6. 안녕테스트 중입니다

### 5. 점수 확인

==================================================================

번호를 입력하세요: 4
최고 점수: 20.0

==================================================================

### 6. 파일 저장/불러오기
save,load는 services에서 save.py로 따로 구현
변수이름 변경, quizzes = quiz , best_score = max_score
### 7. Git 저장소 복제 실습

test code

nangrapigood2005@c5r8s3 mission % rm -r python-mission-clone
override r--r--r-- nangrapigood2005/nangrapigood2005 for python-mission-clone/.git/objects/pack/pack-9f27673ba17676fcdc1763bbe5802702a1eb29fd.idx? 
override r--r--r-- nangrapigood2005/nangrapigood2005 for python-mission-clone/.git/objects/pack/pack-9f27673ba17676fcdc1763bbe5802702a1eb29fd.pack? 
override r--r--r-- nangrapigood2005/nangrapigood2005 for python-mission-clone/.git/objects/pack/pack-9f27673ba17676fcdc1763bbe5802702a1eb29fd.rev? 
rm: python-mission-clone/.git/objects/pack: Directory not empty
rm: python-mission-clone/.git/objects: Directory not empty
rm: python-mission-clone/.git: Directory not empty
rm: python-mission-clone: Directory not empty
nangrapigood2005@c5r8s3 mission % git clone git@github.com:nengrafi/python-mission.git python-mission-clone
fatal: 대상 경로가('python-mission-clone') 이미 있고 빈 디렉터리가 아닙니다.
nangrapigood2005@c5r8s3 mission % git clone git@github.com:nengrafi/python-mission.git python-mission-copy
'python-mission-copy'에 복제합니다...
remote: Enumerating objects: 85, done.
remote: Counting objects: 100% (85/85), done.
remote: Compressing objects: 100% (48/48), done.
remote: Total 85 (delta 31), reused 82 (delta 28), pack-reused 0 (from 0)
오브젝트를 받는 중: 100% (85/85), 150.02 KiB | 410.00 KiB/s, 완료.
델타를 알아내는 중: 100% (31/31), 완료.
nangrapigood2005@c5r8s3 mission % cd python-mission-copy 
nangrapigood2005@c5r8s3 python-mission-copy % code .
nangrapigood2005@c5r8s3 python-mission-copy % git push origin main
오브젝트 나열하는 중: 5, 완료.
오브젝트 개수 세는 중: 100% (5/5), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (3/3), 완료.
오브젝트 쓰는 중: 100% (3/3), 297 bytes | 297.00 KiB/s, 완료.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:nengrafi/python-mission.git
   07d3ecb..1819153  main -> main

nangrapigood2005@c5r8s3 python-mission % git pull origin main
github.com:nengrafi/python-mission URL에서
 * branch            main       -> FETCH_HEAD
업데이트 중 07d3ecb..1819153
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
## 트러블 슈팅 

### 1. Exception 처리시에 프로그램이 종료되지 않음
기존에는 exception.py에서 예외처리시에 return None을 사용하여서 처리했음

이렇게 되니 프로그램이 종료되지 않고 종료시키려면 모든 input에 대해서 예외 처리를 해야하는 상황 발생

따라서 raise를 이용해서 error을 다시 던지고 main.py에서 while 구문을 try-except로 감싸서 예외 처리

### 2. 함수 순서 문제

print(f"최고 점수: {self.data["max_score"]}") 

여기에서 ""내에 ''를 사용했더니 문자열이 일찍 끝난걸로 착각을 해서 오류가 일어남

print(f"최고 점수: {self.data['max_score']}") 

로 수정
