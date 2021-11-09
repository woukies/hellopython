n = float(input("변환할 키로그램(kg)은? "))

print("-" * 50)
print("킬로그램\t파운드\t온스")
print("-" * 50)
print("%.0f\t\t%.2f\t%.2f" % (n, n * 2.204623, n * 35.273962))
print("-" * 50)
