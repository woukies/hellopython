start = int(input("시작 수는? "))
end = int(input("끝 수는? "))
middle = int(input("정수를 입력하세요: "))

if start < middle < end:
    print("%d은(는) %d ~ %d 사이에 있다." %(middle, start, end))
else:
    print("%d은(는) %d ~ %d 사이에 없다." %(middle, start, end))