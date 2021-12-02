name = input("이름을 입력하세요: ")
work = int(input("일주일간 일한 시간을 입력하세요: "))
overwork = 0

if work > 40:
    overwork = work - 40

print("- 이름: %s" % name)
print("- 일주일간 일한 시간: %d시간" % work)
print("- 오버타임: %d시간" % overwork)
print("- 주급: %d원" % (work * 12000 + overwork * 6000))
