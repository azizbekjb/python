#Lambda funksiya
import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi, 10))
def daraja(n):
    return lambda x : x**n
kvadrat = daraja(2)
kub = daraja(3)
print(f"3 -ning kvadrati: {kvadrat(3)}")
print(f"3 -ning kubi: {kub(3)}")
#Natija:
    #62.83185307179586
    # 3 -ning kvadrati: 9
    # 3 -ning kubi: 27
