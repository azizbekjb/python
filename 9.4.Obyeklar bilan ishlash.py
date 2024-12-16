#9.4.Obyektlar bilan ishlash
#Classlar yaratishni boshlash
class Talaba:
    '''Talaba nomli sinf yaratish'''
    def __init__(self, ism, familiya, t_yil):
        '''Obyekt xususiyatlari'''
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.bosqich = 1 #'bosqich' nomli xusisyatgan standart qiymat berish
    #Classga metod qo'shish

    def get_info(self):
        return f"{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi talabasi"
    def set_bosqich(self, bosqich):
        '''Talabaning kursini yangilovchi metod'''
        self.bosqich = bosqich
    def update_bosqich(self):
        '''Talabaning kursini birga oshirish'''
        self.bosqich += 1

#Classdan obyekt yaratish
talaba1 = Talaba('Azizbek', 'Jabborov', 2006)
#Metodlardan foydalanish
print(talaba1.get_info())
#Standart qiymatni o'zgartirish
talaba1.bosqich = 2
print(talaba1.get_info())

talaba1.set_bosqich(3)
print(talaba1.get_info())
'''Talabaning kursini birga oshirish'''
talaba1.update_bosqich()
print(talaba1.get_info())
#Natija:
    # Azizbek Jabborov 1-bosqich talabasi talabasi
    # Azizbek Jabborov 2-bosqich talabasi talabasi
    # Azizbek Jabborov 3-bosqich talabasi talabasi
    # Azizbek Jabborov 4-bosqich talabasi talabasi
