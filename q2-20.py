number = input("하이픈(-)이 포함된 11자리의 휴대폰 번호는? ")

print("- 입력된 휴대폰 번호:", number)
print("- 하이픈 삭제된 휴대폰 번호:", number.replace("-", ""))

phone = number[0:3] + number[4:8] + number[9:]
print("- 하이픈 삭제된 휴대폰 번호:", phone)
