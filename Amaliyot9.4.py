#Amaliyot9.4
class Avto:
    def __init__(self, model, rang, karobka, narx):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.kilometr = 0
    def get_info(self):
        return f"{self.rang} rangli {self.model} mashinasi. Karobkasi {self.karobka}. \n" \
               f"{self.kilometr} km yurgan.\n" \
               f"{self.narx}$ ga baholanmoqda"
    def update_km(self, km):
        self.kilometr += km
    def update_narx(self, javob1, javob2, nx):
        if javob1 == 'ha' and javob2 == 'oshirish':
            self.narx += nx
        elif javob1 == 'ha' and javob2 == 'kamaytirish':
            self.narx -= nx
avto1 = Avto('Gentra', 'Oq', 'Mexanik', 9100)
print(f"Avto narxi: {avto1.narx}$")
javob = input("Avtomobil narxini o'zgartirasimi?: ")
if javob == 'ha':
    javob1 = input('Oshirish yoki kamaytirish?: ')
    if javob1.capitalize() == 'Oshirish':
        miqdor = input("Qanchaga?: ")
        avto1.update_narx(javob, javob1, float(miqdor))
    elif javob1.capitalize() == 'Kamaytirish':
        miqdor = input("Qanchaga?: ")
        avto1.update_narx(javob, javob1, float(miqdor))
javob = input("Avtomobil necha km yurgan?: ")
avto1.update_km(int(javob))
print(avto1.get_info())
#Natija:
    # Avto narxi: 9100$
    # Avtomobil narxini o'zgartirasimi?: ha
    # Oshirish yoki kamaytirish?: kamaytirish
    # Qanchaga?: 2300
    # Avtomobil necha km yurgan?: 170000
    # Oq rangli Gentra mashinasi. Karobkasi Mexanik. 
    # 170000 km yurgan.
    # 6800.0$ ga baholanmoqda
