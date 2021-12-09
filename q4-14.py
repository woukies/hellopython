num = 1
max = 100
sum = 0
line = 1

while num <= 100:
    sum += num
    print("%5d " % sum, end="")
    num += 2
    if line >= 10:
        print()
        line = 1
    else :
        line += 1
