line = 0

for i in range(200, 801):
    if i % 5 != 0:
        print("%d" % i, end=" ")
        line += 1
        if line % 10 == 0:
            print()