#Amaliyot8.3.6
from math import*
def fibonachchi(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, i = 0, 3
    b = 1
    f = [a, b]
    while i <= n:
        a, b = b, a + b
        i += 1
        f.append(b)
    return f
n = int(input("Miqdorni kiriting: "))
print(f"Natija: {fibonachchi(n)}")
