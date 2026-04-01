peo, b = map(int, input().split())
b -= 1
ring = []
final = []

for i in range(1, peo + 1):
    ring.append(i)

# 사람 링 안에 집어 넣기.final.append(ring.pop(b))
for i in range(1, 2 * peo + 1): 
    if i % 2 != 0: # 원상태
        mr = ring[:b] # 앞
        mmr = ring[b:] # 뒤
        mr += mmr # 원상태
        ring = mr
        final.append(ring.pop(b))
    else: # 반대
        mr = ring[:b] # 앞
        mmr = ring[b:] # 뒤
        mmr += mr # 반대
        ring = mmr
    if len(ring) == 0:
        break
    elif len(ring) <= b and len(ring) >= 1:
        break
    elif len(ring) == 1:
        final.append(ring.pop())


if len(ring) != 0:
    if peo % 2 != 0:
        ring.sort()
        while len(ring) == 0:
            ring = ring * b
            final.append(ring.pop(b))
    else:
         while len(ring) == 0:
            ring = ring * b
            final.append(ring.pop(b))

print(ring)     
print(final)
