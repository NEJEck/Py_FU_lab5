s = input()
s1 = ''
for i in range(len(s)-1):
    s1 = s1 + s[i] + '*'
s1 += s[-1]
print(s1)
