i = 1
max = 50

print("-" * 50)
print("\tcm\tmm\tm\tinch")
print("-" * 50)

for i in range(1, max + 1):
    print("\t%d\t%d\t%.2f\t%.2f" % (i, i * 10, i * 0.01, i * 0.393701))
    i += 1

print("-" * 50)
