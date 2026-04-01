a, b = map(int, input().split())
ring = [] # 사람 수 받는 리스트
final=[] # 출력 리스트



for i in range(1, a + 1):
    ring.append(i)

ring *= b

while len(ring) != 0:
    if len(ring) <= b:
        break
    c = ring.pop(b - 1)
    del ring[:b - 1]
    while c in ring:
        ring.remove(c)
    final.append(c)

print(ring)
print(final)