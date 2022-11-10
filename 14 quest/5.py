x = 3
while True:
    if int("121", x) + 1 == int("101", 7):
        print(x)
        break
    x += 1

x_3 = []
while x != 0:
    x_3.insert(0, x % 3)
    x //= 3
print(x_3)