#Klasslarni modulga solish
#9.6:Inkapsulatsiya
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

    @classmethod    #@classmethod-bu maxsus dekorator.Dekorator - o'z ishiga funksiya oluvchi funksiya
    def get_num_avto(cls):
        return cls.__num_avto
