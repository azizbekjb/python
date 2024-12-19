#Amaliyot9.5
#1,2,3,4-masalalar
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
        self.fanlar = []

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

    def fanga_yozil(self, talaba):
        """Talabani fanga qo'shish"""
        self.fanlar.append(talaba)

    def remove_fan(self, fan):
        for element in self.fanlar:
            if element.nomi == fan:
                self.fanlar.remove(element)
            return "Bu fan o'chirildi"
        else:
            return f"Bu fanga siz yozilmagansiz!"

class Fan:
    """Fan classi"""
    def __init__(self, nomi):
        self.nomi = nomi

fan1 = Fan("Algoritmik tillar va dasturlash")
fan2 = Fan("Algoritmlar va berilganlar strukturasi")
fan3 = Fan("Parallel dasturlash")
talaba1 = Talaba("Azizbek", "Jabborov", 'AA0000000', 2006, 1110001)
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)

javob = input("Qaysi fanni o'chirmoqchsiz?: ")
print(talaba1.remove_fan(javob))
print(talaba1.fanlar)
#Natija:
    # Qaysi fanni o'chirmoqchsiz?: Algoritmik tillar va dasturlash
    # Bu fan o'chirildi
    # [<__main__.Fan object at 0x000001E60F98BDA0>, <__main__.Fan object at 0x000001E60F98BDD0>]
