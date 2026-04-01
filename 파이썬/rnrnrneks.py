a = int(input())

for i in range(a, a + 1):
    for j in range(1, 10):
        c = i * j
        print("%d X %d = %d"%(i, j, c))