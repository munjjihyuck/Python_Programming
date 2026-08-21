# 변수
# 동적 타이핑 언어
a = 2
b = 3
print(a, end="")
print(b)
print(a, b, sep=",")

x = y = z = 0

a, b = 2, 3  # 튜플 언패킹
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 문자, 숫자, 언더바만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가

이름 = "홍길동"
print(이름)
# 한글 변수도 가능

student_name = "홍길동"
studentName = "홍길동"
MAX_COUNT = 100
