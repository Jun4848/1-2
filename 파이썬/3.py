a, b = map(int, input().split())
c = []
d = []
e = 0
for i in range(1, a + 1):
    c.append(i)


for i in range(1, a + 1):
    d.append(c.pop(2))

print(d)    