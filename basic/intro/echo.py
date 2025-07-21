def main():
    while True:
        user_input = input("문장을 입력하세요: ")

        if user_input == "!quit":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break

        print("입력하신 문장은: ", user_input)

if __name__ == "__main__":
    main()