a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

result = a + b

print("%d + %d = %d" % (a, b, result))
if result % 3 == 0:
    print("%d은(는) 3의 배수이다." % result)
else:
    print("%d은(는) 3의 배수가 아니다." % result)
