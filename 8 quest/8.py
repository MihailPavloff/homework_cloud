from itertools import product

p = list(product("ЕГЭ", repeat=5))
p = list(map("".join, p))

n = 0

for i in p:
    if i[0] == 'Е' or i[0] == 'Э':
        n += 1

print(n)