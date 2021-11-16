n1 = int(input("첫 번째 숫자를 입력하세요: "))
n2 = int(input("두 번째 숫자를 입력하세요: "))
print("원하는 연산은?")
operator = input("+, -, *, / 중 하나를 선택하세요: ")

if operator == '+':
    print("%d + %d = %d" % (n1, n2, n1 + n2))
elif operator == '-':
    print("%d - %d = %d" % (n1, n2, n1 - n2))
elif operator == '*':
    print("%d * %d = %d" % (n1, n2, n1 * n2))
elif operator == '/':
    print("%d / %d = %d" % (n1, n2, n1 / n2))
else:
    print("선택 오류!")
