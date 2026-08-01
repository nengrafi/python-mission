from models.quiz import Quiz
from services.save import load

data = load()

max_score = data["max_score"]

for item in data["quiz"]:
    quiz = Quiz(item["question"],item["choices"],item["answer"])
    quiz.display()
    quiz.Correct()
