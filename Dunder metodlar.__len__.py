#Dunder metodlar
#Dunder -- Double UNDERScore -->dunder
#print(dir(Avto))
#Obyekt uzunlig: '__len__ metodi
#isinstance metodi->Tegishlilik metodi
#print(isinstance(1, int))
#Natija:
    #True-> chunki 1 bu butun son
from uuid import uuid4
class Avto:
    # __ belgilari klasning xususiyatlarni inkapsulatsiya qilish uchun ishlatiladi
    __num_avto = 0
    def __init__(self,make, model, rang, yil, narx, km = 0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1    #__init metodiga murojaat qilganda bu xususiyat qiymati bittaga oshadi
        #uuid4() har bir obyekt uchun noyob va takrorlanmas id yaratish

    def get_km(self):
        return self.__km
    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            return "Mashina km kamaytirib bo'lmaydi"
    def get_id(self):
        return self.__id

    #Obyekt haqida ma'lumot.Ya'ni tushinarli ma'lumot chiqarish
    def __repr__(self):
        '''Obeykt haqida ma'lumot'''
        return f"Avto: {self.rang} {self.make} {self.model}"

    def __eq__(self, boshqa_avto):
        '''Tenglik'''
        return self.narx == boshqa_avto.narx

    def __lt__(self, boshqa_avto):
        '''Kichik'''
        return self.narx < boshqa_avto.narx

    def __le__(self, boshqa_avto):
        '''Kichik yoki teng'''
        return self.narx <= boshqa_avto.narx

    #Qolgan taqqoslash metodlari xuddi shu tarzda yoziladi
    @classmethod    #@classmethod-bu maxsus dekorator.Dekorator - o'z ishiga funksiya oluvchi funksiya
    def get_num_avto(cls):
        return cls.__num_avto
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def add_auto(self, avto):
        if isinstance(avto, Avto):
            self.avtolar.append(avto)
        else:
            print("Avto abyektini kiriting")

    def __len__(self):
        return len(self.avtolar)
avto1 = Avto("GM", "Gentra", "Oq", 2019, 9100)
avto2 = Avto("Mercedes", "W124", "Qora", 1993, 12000)
avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
salon1 = AvtoSalon("MaxAvto")
# Yuqoridagi obyektlarni salon1 ga qo'shamiz
for avto in [avto1, avto2, avto3]:
    salon1.add_auto(avto)
print(salon1.avtolar)
print(len(salon1))
#Natija:
    # [Avto: Oq GM Gentra, Avto: Qora Mercedes W124, Avto: Silver Toyota Carolla]
    # 3 Salonimizdagi 3 ta mashina bor
    # Bu yerda len() metodi AvtoSalon klasidagi abyektlar uchun boshqacha ishlaydi
