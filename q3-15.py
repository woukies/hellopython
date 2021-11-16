a = input("문자열을 입력하세요: ")
aLen = len(a)

if aLen % 2 == 0:
    result = "짝수"
else:
    result = "홀수"

print("문자열의 개수:", aLen)
print("문자열의 개수는 %s이다" % result)
