book = int(input("책 값은? "))
discount = int(input("할인율은? "))
delivery = int(input("배송료는? "))

print("책 값: %d원" % book)
print("할인율: %d" % discount)
print("배송료: %d원" % delivery)
print("결제 금액: %d원" % (book * (100 - discount) / 100 + delivery))
