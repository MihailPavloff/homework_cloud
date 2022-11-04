from itertools import permutations

p = list(permutations("ВУАЛЬ"))
p = list(map("".join, p))

n = 0
for word in p:
    if word.startswith("Ь") or "ЬУ" in word or "ЬА" in word:
        continue
    n += 1

print(n)
