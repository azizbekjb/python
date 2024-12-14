#Moslashuvchi funksiya: *args
#*args bu arguments
def summa(*sonlar):
    """Bir nechta sonlarni yig'indisini topuvchi dastur"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(f"Yig'indi: {summa(2,3,3)}")#Istalgancha parametr chaqirish mumkin
#Dasturni sodda varianti:
    # def summa(sonlar):
    #     """Bir nechta sonlarni yig'indisini topuvchi dastur"""
    #     return sum(sonlar)
#Natija:
    #Yig'indi: 8
