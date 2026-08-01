import json

def load():
        try:
            with open("data/state.json","r",encoding="utf-8") as f:
                return json.load(f)

        except FileNotFoundError:
            print("파일이 존재하지 않습니다. 기본 데이터를 사용합니다.\n")

        except json.JSONDecodeError:
            print("파일이 손상되었습니다. 기본 데이터를 사용합니다.\n")

        with open("data/example.json","r",encoding="utf-8") as f:
            return json.load(f)

def save(data):
    #ensure_ascii는 사람이 읽기 불가능 하게 하는것, indent로 4칸 들여쓰기 
    with open("data/state.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)