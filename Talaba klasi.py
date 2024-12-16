#Talaba klasi
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

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning to'liq ism-familyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
        # Argument qabul qiluvchi metod

    def get_age(self, yil):
        """Talabaning yoshini qaytardi"""
        return yil - self.t_yil
