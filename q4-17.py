count = 1
num = 1
max = 1000

while num <= max:
    if num % 3 != 0:
        print("%4d " % num, end="")
        count += 1
        if count % 10 == 0:
            print()
    num += 1
