import requests

def get_github_user(username, token=None):
    """
    GitHub 사용자 정보를 가져오는 함수.
    인증 토큰을 사용하면 rate limit을 회피할 수 있음.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {"error": "존재하지 않는 GitHub 사용자입니다."}
        return {"error": f"HTTP 오류 발생: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"요청 실패: {req_err}"}


def validate_github_user(username, token=None):
    """
    사용자 정보 조회 결과를 테스트하고 메시지 출력
    """
    result = get_github_user(username, token)
    print(result)
    if "error" in result:
        print(f"❌ 사용자 '{username}' 테스트 실패: {result['error']}")
    elif "login" in result:
        print(f"✅ 사용자 '{username}' 테스트 성공")
    else:
        print(f"❌ 사용자 '{username}' 테스트 실패: 예상치 못한 응답")


if __name__ == "__main__":
    token = "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"

    username = input("유저 아이디 입력: ").strip()
    validate_github_user(username, token)
