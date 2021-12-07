s = "Python is widely used by a number of big companies"
sIndex = 0
res = ""

while sIndex < len(s):
    if s[sIndex] == 'a' or s[sIndex] == 'e' or s[sIndex] == 'i' or s[sIndex] == 'o' or s[sIndex] == 'u':
        res += (s[sIndex] + " ")
    sIndex += 1

print("모음: %s" % res)
print("모음 개수: %d" % len(res.split()))

sIndex = 0
count = 0
print("모음: ", end="")
while sIndex < len(s):
    if s[sIndex] == 'a' or s[sIndex] == 'e' or s[sIndex] == 'i' or s[sIndex] == 'o' or s[sIndex] == 'u':
        print(s[sIndex], end=" ")
        count += 1
    sIndex += 1

print()
print("모음 개수: %d" % count)
