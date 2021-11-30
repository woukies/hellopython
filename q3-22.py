firstHour = int(input("첫 번째 시간의 시를 입력하세요: "))
firstMinute = int(input("첫 번째 시간의 분을 입력하세요: "))
secondHour = int(input("두 번째 시간의 시를 입력하세요: "))
secondMinute = int(input("두 번째 시간의 분을 입력하세요: "))

first = firstHour * 60 + firstMinute
second = secondHour * 60 + secondMinute

if first <= second:
    print("- 빠른 시간: %d:%d" % (firstHour, firstMinute))
    print("- 늦은 시간: %d:%d" % (secondHour, secondMinute))
else:
    print("- 빠른 시간: %d:%d" % (secondHour, secondMinute))
    print("- 늦은 시간: %d:%d" % (firstHour, firstMinute))
