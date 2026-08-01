import json

def load():
    try:
        with open("data/data.json","r",encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print("파일이 존재하지 않습니다. 기본 데이터를 사용합니다.\n")

    except json.JSONDecodeError:
        print("파일이 손상되었습니다. 기본 데이터를 사용합니다.\n")

    with open("data/example.json","r",encoding="utf-8") as f:
        return json.load(f)

