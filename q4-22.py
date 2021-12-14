num = input("숫자를 입력하세요: ")
cnt = 0

for i in range(len(num)):
    if int(num[i]) % 2 != 0:
        cnt += 1

print("홀수의 개수: %d개" % cnt)
