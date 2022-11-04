from itertools import product

p = list(map("".join, list(product("УОА", repeat=5))))
print(p[239])