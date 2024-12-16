#9.3:Klasslar
#Classlar yaratishni boshlash
class Talaba:
    '''Talaba nomli sinf yaratish'''
    def __init__(self, ism, familiya, t_yil):
        '''Obyekt xususiyatlari'''
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
    #Classga metod qo'shish
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.t_yil}-yilda tug'ilganman")
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    def get_fullname(self):
        """Talabaning to'liq ism-familyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    #Argument qabul qiluvchi metod
    def get_age(self,yil):
        """Talabaning yoshini qaytardi"""
        return yil - self.t_yil
    #Tayyor bo'lmagan metodlar
    def describe():
        #To'ldirish uchun pass operatori ishlatiladi
        pass
    def get_email():
        pass


#Classdan obyekt yaratish
talaba1 = Talaba('Azizbek', 'Jabborov', 2006)
#Obyekt xususiyatlariga murojat etish
print(talaba1.ism, talaba1.familiya, talaba1.t_yil,'-yilda tug\'ilgan')

#Metodlardan foydalanish
print(talaba1.get_name())
print(talaba1.get_lastname())

talaba1.tanishtir()

print(f"Yoshim {talaba1.get_age(2024)} yoshda")
