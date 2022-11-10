a = 64 ** 10 + 2 ** 90 - 14
print(a)

num_8 = []
while a != 0:
    num_8.insert(0, a % 8)
    a //= 8

print(num_8.count(7))