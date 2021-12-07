phone = input("하이픈(-)=을 포함한 휴대폰 번호를 입력하세요: ")

print(phone.replace("-", ""))

for s in phone:
    if s != "-":
        print(s, end="")
