#7.2. exceptions(istisnolar)
#Bir nechta xatolarni ushlash
n = input("Butun son kiritng: ")
try:
    n = int(n)
    x = 20 / n
except ValueError:#Agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError:#Agar foydalanuvchi 0  kiritmasa
    print("0 ga bo'lib bo'lmaydi!")
else:
    print(f"x={x}")
#Natija:
    #1-shart:
        #Butun son kiritmadingiz
    #2-shart:
        #0 ga bo'lib bo'lmaydi!
    #3-shart:
        #x = 6.666666666666667
