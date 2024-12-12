#Amaliyot8.3.5     
from math import*
def tub_son(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a ,b =map(int, input("Oraliqni kiriting: ").split())
for i in range(a, b+1):
    if tub_son(i):
        print(i, end=' ')
#Natija:
    # 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53
