month = int(input("월을 숫자로 입력하세요: "))

if month == 3 or month == 4 or month == 5:
    season = "봄"
elif 6 <= month <= 8:
    season = "여름"
elif 9 <= month <= 11:
    season = "가을"
else:
    season = "겨울"

print("%d월은 %s입니다." % (month, season))
