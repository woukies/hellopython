dollar = 10
max = 100

print("-" * 40)
print("\t달러\t원화\t유로")
print("-" * 40)
while dollar <= max:
    print("\t%d\t%d\t%.1f" % (dollar, dollar * 1080, dollar * 0.81))
    dollar += 10
print("-" * 40)
