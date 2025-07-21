import re

def validate_password(password):
    if len(password) < 8:
        return "비밀번호는 최소 8자 이상이어야 합니다."
    
    if not re.search(r"[a-z]", password):
        return "비밀번호는 최소 한 개의 영문 소문자를 포함해야 합니다"
    
    if not re.search(r"[A-Z]",password):
        return "비밀번호는 최소 한 개의 영문 대문자를 포함해야 합니다."

    if not re.search(r"[0-9]",password):
        return "비밀번호는 최소 한 개의 숫자를 포함해야 합니다." 

    if not re.search(r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", password):
        return "비밀번호는 최소 한 개의 숫자를 포함해야 합니다." 
    
    return "비밀번호가 유효합니다"

def main():
    while True:
        password = input("사용하실 비밀번호를 입력하세요: ")
        result = validate_password(password)
        if result == "비밀번호가 유효합니다":
            print(result)
            break

        print(result)

if __name__ == "__main__":
    main()