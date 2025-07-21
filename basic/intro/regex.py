import re

def validate_password(password):
    if len(password) < 8:
        return "비밀번호는 최소 8자 이상이어야 합니다."
    