#Klasslarni modulga solish
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
class Professor(Shaxs):
    """Professor klassi"""
    def __init__(self, ism, familiya, passport, tyil, ish_joyi, mutaxasisligi):
        super().__init__(ism, familiya, passport, tyil)
        self.ish_joyi = ish_joyi
        self.mutaxasisligi = mutaxasisligi

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Ish joyi: {self.ish_joyi}.\n" \
                f"Mutaxasisligi: {self.mutaxasisligi}"

class Foydalnuvchi(Shaxs):
    """Foydalanuvchilar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil, username, parol):
        super().__init__(ism, familiya, passport, tyil)
        self.username = username
        self.parol = parol

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Foydalanuvchi nomi : {self.username}.\n" \
                f"Akkaunt paroli: {self.parol}"

class Admin(Foydalnuvchi):
    """Admin klassi"""
    def __init__(self, ism, familiya, passport, tyil, username, parol):
        super().__init__(ism, familiya, passport, tyil, username, parol)
        self.foydalanuvchilar = []
        self.foydalanuvchilar_soni = 0
        self.blokdagilar = 0

    def admin_qosh(self, foydalanuvchi):
        self.foydalanuvchilar.append(foydalanuvchi)
        self.foydalanuvchilar_soni += 1

    def block_user(self, user):
        print(f"{user.username} siz bizni qoidalarimizni buzdingiz.\n"
              f"Shu sababli siz bloklandingiz. Blokdan chiqish uchun 10 kun kutishingiz kerak bo'ladi")
        self.blokdagilar += 1

    def hisobot_ber(self):
        print(f"Platformamizdagi foylanuvchilar soni: {self.foydalanuvchilar_soni}\n"
              f"Blokdagilar soni: {self.blokdagilar}")
