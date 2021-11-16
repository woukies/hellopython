age = int(input("나이는? "))

fee = 2000
if age >= 65:
    fee = 0

print("나이: %d세" % age)
print("입장료: %d원" % fee)
