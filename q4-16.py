s = input("문장을 입력해 주세요: ")
c = len(s) - 1

while c >= 0:
    if s[c] == " ":
        print("-", end="")
    else:
        print(s[c], end="")
    c -= 1