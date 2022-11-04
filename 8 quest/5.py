from itertools import product

p = list(map("".join, list(product('ВЕСНА', repeat=3))))

n = 0

for i in p:
    if "А" in i:
        n += 1
print(n)

