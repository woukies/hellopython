max = 10
for i in range(1, max):
    for j in range(max - i):
        print(max - i, end=" ")
    print()

for i in range(9, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()