def input_number(message:str,min_num:int,max_num:int):
    while True:
        try:
            text = input(message).strip()

            if text == "":
                print("값을 입력해주세요")
                continue

            text_int = int(text)

            if text_int < min_num or text_int > max_num:
                print(f"범위 밖의 입력입니다 ({min_num} ~ {max_num}.)")
                continue

            if text == "":
                print("값을 입력해주세요")
                continue

            return text_int

        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        except KeyboardInterrupt:
            print("KeyboardInterrupt가 발생했습니다. 프로그램을 안전하게 종료합니다.")
            return None
        
        except EOFError:
            print("EOFError가 발생했습니다. 프로그램을 안전하게 종료합니다.") 
            return None