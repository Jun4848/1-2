a = [1,2,3,4,5,6,7]
d = []

e = 3
e -= 1

for i in range(1,5):
    if i % 2 == 0 :
        b = a[3:] # 뒤
        c = a[:3] # 앞
        b += c
        d.append(a.pop(e))
        b = a[3:]
        c = a[:3]
        c += b
    else:
        d.append(a.pop(e))
print(d)