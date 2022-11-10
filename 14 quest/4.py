a = 4 ** 2015 + 8 ** 405 - 2 ** 150 - 122
num_2 = []
while a != 0:
    num_2.insert(0, a % 2)
    a //= 2
print(num_2.count(1))