#9.5.Vorislik va polimorfizm
#Voris klasslarga xos xususiyatlar va metodlar.Polimorfizm
#Super - klass metodlarini qayta yozish
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
    def __init__(self, ism, familiya, passport, tyil, id):
        """Talaba xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = id
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
shaxs1 = Shaxs("Azizbek", "Jabborov", 'AA0000000', 2006)
print(f"{shaxs1.get_info()}. {shaxs1.get_age(2024)} yoshda")

talaba1 = Talaba("Azizbek", "Jabborov", 'AA0000000', 2006, 1110001)
print(talaba1.get_info())
print(talaba1.get_age(2024))
#Natija:
    # Azizbek Jabborov. Passport: AA0000000, 2006-yilda tug'ilgan. 18 yoshda
    # Azizbek Jabborov. 2-bosqich. ID: 1110001
    # 18
