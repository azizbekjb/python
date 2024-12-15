#map() funksiyasi
from math import sqrt
sonlar = list(range(0, 11))
ildizlar = list(map(sqrt, sonlar))
print(f"Ildizlar: {ildizlar}")

def daraja2(x):
    return x*x
print(f"Darajalar : {list(map(daraja2, sonlar))}")

a = [1, 2, 3]
b = [4, 5, 6]
a_plus_b = list(map(lambda x, y: x + y, a, b))
print(f"Ikki ro'yxat mos elementlari yig'indisi : {a_plus_b}")
#Natija:
# Ildizlar: [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]
# Darajalar : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [5, 7, 9]
