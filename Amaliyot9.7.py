#Amaliyot9.7

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

    def __repr__(self):
        return f"Shaxs: {self.ism} {self.familiya}. {2024 - self.tyil} yoshda"

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, bosqich, id):
        """Talaba xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = id
        self.bosqich = bosqich
    #Kichik
    def __lt__(self, boshqa):
        return self.bosqich < boshqa.bosqich

    #Teng
    def __eq__(self, boshqa):
        return self.bosqich == boshqa.bosqich


class Fan:
    """Fan classi"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []

    def add_student(self, *talaba):
        """Talabani fanga qo'shish"""
        for t in talaba:
            self.talabalar.append(t)

    def __getitem__(self, index):
        return self.talabalar[index]

    def __setitem__(self, index, qiymat):
        if isinstance(qiymat, Talaba):
            self.talabalar[index] = qiymat
        else:
            print("Talaba obyektini kiriting")

    def __len__(self):
        return len(self.talabalar)
    #Qo'shish
    def __add__(self, qiymat):
        if isinstance(qiymat, Talaba):
            self.talabalar.append(qiymat)
        else:
            print("Talaba obyektini kiriting")

    #Ayirish
    def __sub__(self, qiymat):
        if isinstance(qiymat, Talaba):
            for talaba in self.talabalar:
                if qiymat.passport == talaba.passport:
                    return self.talabalar.remove(qiymat)
        else:
            return "Passport seriyani to'g'ri kiriting"

    def __call__(self, *param):
        if param:
            for talaba in param:
                self.add_student(talaba)
        else:
            return [talaba for talaba in self.talabalar]

fan1 = Fan("Algoritmik tillar va dasturlash")
talaba1 = Talaba("Azizbek", "Jabborov", 'AA0000000', 2006, 2,"1110001")
talaba2 = Talaba("Sardor", "Tolliboyev", "AB1234567", 2007, 2, "1110000")
talaba3 = Talaba("Salim", "Valiyev", "AO7654321", 2001, 4, "11110010")
print(talaba1) #!- talaba haqida ma'lumot
print(talaba1 < talaba2) # Talabalar kursini taqqoslash
fan1.add_student(talaba1, talaba2, talaba3) #Fanga talabalarni qo'shish
print(fan1[:])
new_student = Talaba("Ulug'bek", "Ravshanov", "AA1221111", 2006, 1, "1111111")

fan1 + new_student #Fanga yangi talabani qo'shish
print(fan1()) #Yangi ro'yxatni chop etish
fan1 - talaba3 #Fandan talabani olib tashlash
print(fan1()) # Oxirgi natija
#Natija:
    # Shaxs: Azizbek Jabborov. 18 yoshda
    # False
    # [Shaxs: Azizbek Jabborov. 18 yoshda, Shaxs: Sardor Tolliboyev. 17 yoshda, Shaxs: Salim Valiyev. 23 yoshda]
    # [Shaxs: Azizbek Jabborov. 18 yoshda, Shaxs: Sardor Tolliboyev. 17 yoshda, Shaxs: Salim Valiyev. 23 yoshda, Shaxs: Ulug'bek Ravshanov. 18 yoshda]
    # [Shaxs: Azizbek Jabborov. 18 yoshda, Shaxs: Sardor Tolliboyev. 17 yoshda, Shaxs: Ulug'bek Ravshanov. 18 yoshda]
