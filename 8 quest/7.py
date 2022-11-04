from itertools import product

p = list(map("".join, list(product("ACGT", repeat=5))))
print(p)

n = 0
for i in p:
    if i.count("A") == 2:
        n += 1

print(n)