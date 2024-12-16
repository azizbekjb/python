#Amaliyot9.4
class Avto:
    def __init__(self, model, rang, karobka, narx):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.kilometr = 0
    def get_info(self):
        return f"{self.rang} rangli {self.model} mashinasi. Karobkasi {self.karobka}. " \
               f"{self.kilometr} km yurgan." \
               f"{self.narx}$ ga baholanmoqda"
    def update_km(self, km):
        self.kilometr += km
    def update_narx(self, javob1, javob2, nx):
        if javob1 == 'ha' and javob2 == 'oshirish':
            self.narx += nx
        elif javob1 == 'ha' and javob2 == 'kamaytirish':
            self.narx -= nx

class Avtosalon():
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.sotuvdagi_avtolar = []

    def add_avto(self, avto):
        self.sotuvdagi_avtolar.append(avto)
    def get_avtos(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtolar]
avto1 = Avto('Gentra', 'Oq', 'Mexanik', 9100)
avto2 = Avto("Cobalt", 'Qora', 'Avtomat', 10100)
avto3 = Avto("Tracker", 'Oq', 'Avtomat', 12000)
Firma = Avtosalon("NewCar", 'Samarkand')
Firma.add_avto(avto1)
Firma.add_avto(avto2)
Firma.add_avto(avto3)
for info in Firma.get_avtos():
    print(info)
#Natija:
    # Oq rangli Gentra mashinasi. Karobkasi Mexanik. 0 km yurgan.9100$ ga baholanmoqda
    # Qora rangli Cobalt mashinasi. Karobkasi Avtomat. 0 km yurgan.10100$ ga baholanmoqda
    # Oq rangli Tracker mashinasi. Karobkasi Avtomat. 0 km yurgan.12000$ ga baholanmoqda
