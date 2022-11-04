from itertools import permutations

p = list(permutations('КАПКАН'))
words = []
for i in range(len(p)):
    words.append("".join(p[i]))
n = 0
for x in set(words):
    if 'АА' in x or 'КК' in x:
        continue
    n += 1
    print(x)
print(n)