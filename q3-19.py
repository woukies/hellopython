price = int(input("구매 금액은? "))

print("구매 금액:", price)

if 300000 <= price:
    discount = 10
elif 50000 <= price:
    discount = 7.5
elif 10000 <= price:
    discount = 5
else:
    discount = 0

print("할인율:", discount)
print("할인금액: %.0f" % price * discount / 100)
print("지불금액: %d" % int(price * (100 - discount) / 100)) 
