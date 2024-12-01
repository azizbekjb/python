#       1)Ikkita to'plamning birlashmasi.
#   1.1)'|' operatori
A = {1,3,5,7,9}
B = {2,4,6,8,0}
C = A | B
print(f"Birlashma : {C}")#   {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#   1.2)'.union()' metodi
D = A.union(B)
print(f"Birlashma : {D}")#   {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#       2)Ikki to'plamning kesishmasi
#   2.1)'&" operatori
A = {1,3,3,5,6,4,3}
B = {0,23,2344442,23,4,5,6,7}
E = A & B
print(f"Kesishma {E}")#   {4, 5, 6}
#   2.2)'.intersection' metodi
F = A.intersection(B)
print(f"Kesishma {F}")#   {4, 5, 6}

#       3)To'plamlar ayirmasi
#   3.1.1)'-' operatori:A - B
G = A - B   #   A to'plamning B to'plamda yo'q elementlari
print(f"A - B {G}")#   {1, 3}
#   3.1.2)'-' operatori:B - A
G_1 = B - A
print(f"B - A {G_1}")#  {0, 2344442, 23, 7}
#   3.2.1).difference metodi: A.difference(B)
H = A.difference(B)
print(f"A - B {H}")#   {1, 3}
#   3.2.1).difference metodi: B.difference(A)
H_1 = B.difference(A)
print(f"B - A {H_1}")#  {0, 2344442, 23, 7}

#      4)Simmetrik ayirma.
#   4.1)'^' operatri
J = A ^ B
print(f"A ^ B {J}")#    {0, 1, 3, 7, 23, 2344442}
#   4.2)'symmetric_diference' metodi
J_1 = A.symmetric_difference(B)
print(f"A ^ B {J_1}")#    {0, 1, 3, 7, 23, 2344442}
