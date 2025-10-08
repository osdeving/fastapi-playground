a = [1,2,4, [5,6,7]]
b = a[:]

a[3][0] = 10 # type: ignore

a[0] = 13232
b[0] = 43
print(a)
print(b)
