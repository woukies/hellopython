start = 500
end = 600
sum = 0

while start <= end:
    if start % 5 == 0:
        sum += start
    start += 1

print("5의 배수 합계: %d" % sum)
