#Moslashuvchi funksiya: *args
#*args bu arguments
def summa(x, y, *sonlar):
    """Bir nechta sonlarni yig'indisini topuvchi dastur"""
    #Bu yerda ikkita majburiy kiritiladigan parametr bor: Bular x va y
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return x + y + yigindi
print(f"Yig'indi: {summa(2, 3, 3, 6, 2, 1)}")#Istalgancha parametr chaqirish mumkin.Bosidagi 2 va 3 majburiy parametr
#Natija:
    # Yig'indi: 17 
