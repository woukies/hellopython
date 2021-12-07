line = 50
print("=" * line)
todayYear = int(input("현재년은? "))
todayMonth = int(input("현재월은? "))
todayDay = int(input("현재일은? "))
birthYear = int(input("출생년은? "))
birthMonth = int(input("출생월은? "))
birthDay = int(input("출생일은? "))
print("=" * line)
print("오늘날짜: %d년 %d월 %d일" % (todayYear, todayMonth, todayDay))
print("생년월일: %d년 %d월 %d일" % (birthYear, birthMonth, birthDay))
print("-" * line)

age = todayYear - birthYear
if birthMonth > todayMonth:
    age -= 1
elif birthMonth == todayMonth and birthDay >= todayDay:
    age -= 1

print("만 나이: %d세" % age)
print("=" * line)
