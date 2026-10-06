# 사용자 정의 모듈
print("start:", __name__)
# 모듈의 이름을 가져오는 내장 변수 / 여기서 실행하면 '__main__', 다른곳에서 실행하면 / 'mymath'
PI = 3.14


def add(a, b):
    return a + b


# 직접 실행한 경우
if __name__ == "__main__":
    print(PI)
    print(add(10, 20))
