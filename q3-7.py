c = input("영어 대문자 또는 소문자 하나를 입력하세요: ")
c = c.upper()

# if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
#     print("%c 은(는) 모음이다." % c)
if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print("%c 은(는) 모음이다." % c)
else:
    print("%c 은(는) 자음이다." % c)
