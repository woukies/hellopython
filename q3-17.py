print("기능 선택", "1. 더하기", "2. 빼기", "3. 곱하기", "4. 나누기", "", sep='\n')
operator = input("계산기 기능을 선택하세요(1/2/3/4): ")
n1 = int(input("첫 번째 숫자를 입력하세요: "))
n2 = int(input("두 번째 숫자를 입력하세요: "))

if operator == '1':
    print("%d + %d = %d" % (n1, n2, n1 + n2))
elif operator == '2':
    print("%d - %d = %d" % (n1, n2, n1 - n2))
elif operator == '3':
    print("%d * %d = %d" % (n1, n2, n1 * n2))
elif operator == '4':
    print("%d / %d = %d" % (n1, n2, n1 / n2))
else:
    print("선택 오류!")
