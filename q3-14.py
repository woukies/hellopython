num = input("수를 입력하세요: ")

if len(num) == 1:
    print("%s 은(는) 한 자리 숫자이다." % num)
elif len(num) == 2:
    print("%s 은(는) 두 자리 숫자이다." % num)
elif len(num) == 3:
    print("%s 은(는) 세 자리 숫자이다." % num)
else:
    print("오류! %s 은(는) 범위(0 ~ 999) 이외의 숫자이다." % num)
