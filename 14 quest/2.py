a = 49 ** 7 + 7 ** 21 - 7
print(a)  # изначальное число
num = []
while a != 0:
    num.insert(0, a % 7)
    a //= 7
print(num)  # переведенное в другую систему
result = 0
i = 0
while len(num) != 0:
    a = num.pop(len(num) - 1)
    result += a * 7 ** i
    i += 1

print(result)  # переведенное в изначальную систему
