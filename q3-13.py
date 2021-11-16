num = str(input("숫자를 입력하세요: "))

num4 = int(num[2])

if num4 % 2 == 0:
    result = "짝수"
else:
    result = "홀수"

print("%d은(는) %s이다." % (num4, result))
