import sys

def main():
    try:
        # 讀取輸入並去除前後空白
        user_input = input().strip()
        
        if user_input == "0":
            print("False")
        elif user_input == "1":
            print("True")
        else:
            print("Nooooooooooooooooo!!!")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
