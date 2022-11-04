from itertools import permutations

p = list(map("".join, list(permutations("УЛЕЙ"))))
print(p)

n = 0
for word in p:
    if word[0] == "Й" or "ЕУ" in word:
        continue
    n += 1

print(n)