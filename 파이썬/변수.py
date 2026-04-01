a = [1,2,3]
b = a
print(id(a))

b = a[:]
print(a is b)

(c, d) = 'python', 'life'
print(c, d)

e = f = 'py'
print(e)
print(f)

g = 3
h = 5
g, h = h, g
print(g)
print(h)