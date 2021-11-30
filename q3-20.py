print("서비스 만족도:", " 1: 매우만족", " 2: 만족", " 3: 불만족", sep='\n')
grade = input("서비스 만족도는? (1/2/3) ")
price = int(input("음식 값은? "))

if grade == "1":
    res = "매우만족"
    tip = price * 0.2
elif grade == "2":
    res = "만족"
    tip = price * 0.1
elif grade == "3":
    res = "불만족"
    tip = 0
else:
    res = "잘못된 입력"
    tip = -1

print("서비스 만족도:%s, 팁: %d원" % (res, tip))
