from itertools import product

p = list(map("".join, list(product("СЛОН", repeat=5))))

n = 0
for i in p:
    if i.count('С') == 1:
        n += 1

print(n)