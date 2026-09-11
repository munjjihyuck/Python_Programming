# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("End")  # else는 while문이 false일때 실행 -> break로 강제종료시 실행X

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

# found = False

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found")
        # found = True
        break
    i += 1
else:
    print(f"{target} not found")

# if found == False:
#    prprint(f"{target} not found")

# 1 ~ `10까지의 합
i = 0
tot = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    tot += i
else:
    print(f"sum = {tot}")
