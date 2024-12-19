#9.5.Vorislik va polimorfizm
#Obyekt ichida obyekt
class Shaxs:    #Super klass
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, id, manzil):
        """Talaba xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = id
        self.manzil = manzil
        self.bosqich = 2

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.bosqich}-bosqich. ID: {self.idraqam}"
        return info

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani,"
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

manzil = Manzil(15, "Sahoba", 'Samarqand', 'Samarqand')
talaba1 = Talaba("Azizbek", "Jabborov", 'AA0000000', 2006, 1110001, manzil)
print(talaba1.manzil.get_manzil())
print(talaba1.manzil.viloyat)

#Natija:
    # Samarqand viloyati, Samarqand tumani,Sahoba ko'chasi, 15-uy
    # Samarqand
