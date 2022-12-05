from itertools import product

p = list(map("".join, list(product('АНИУТОПЯ*', repeat=7))))
gl_ = "АИОУЯ"
sogl_ = "НПТ"
count = 0
for word in p:
    if word.count("*") == 1 and word[0] != '*' and word[-1] != '*':
        a = word.index("*")
        flag = False
        for i in gl_:
            if i in word[a:]:
                flag = True
                break
        for i in sogl_:
            if i in word[0:a]:
                flag = True
                break
        if flag:
            continue
        sogl = [y for y in word if y in "НПТ"]
        gl = [y for y in word if y in "АИОУЯ"]
        if sorted(sogl) == sogl and sorted(gl, reverse=True) == gl:
            print(word)
            count += 1

print(count)