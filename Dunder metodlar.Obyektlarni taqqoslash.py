#Dunder metodlar
#Dunder -- Double UNDERScore -->dunder
#print(dir(Avto))
#Obyektlarni taqqoslash: '__lt__', '__le__', '__gt__', '__ge__', '__eq__', '__ne__' metodlari
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
avto1 = Avto("GM", "Gentra", 'OQ', 2019, 9100, 100000)
avto2 = Avto("Mercedes", "W124", 'Qora', 1991, 12000)

#Solishtirish
print(avto1 < avto2)
print(avto1 == avto2)
print(avto1 <= avto2)
#Natija:
    # True
    # False
    # True
