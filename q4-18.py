print("-" * 20)
print(" 섭씨\t화씨")
print("-" * 20)
for degree in range(-20, 31, 5):
    print("%5d\t%6.1f" % (degree, (degree * 9 / 5) + 32))

print("-" * 20)
