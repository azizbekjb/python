#9.4:Obyektlar o'rtasidagi munosabat
#Classlar yaratishni boshlash
class Talaba:
    '''Talaba nomli sinf yaratish'''
    def __init__(self, ism, familiya, t_yil):
        '''Obyekt xususiyatlari'''
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.bosqich = 1 #'bosqich' nomli xusisyatgan standart qiymat berish
    #Classga metod qo'shish

    def get_info(self):
        return f"{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi talabasi"
    def set_bosqich(self, bosqich):
        '''Talabaning kursini yangilovchi metod'''
        self.bosqich = bosqich
    def update_bosqich(self):
        '''Talabaning kursini birga oshirish'''
        self.bosqich += 1

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    def add_student(self, talaba):
        '''Fanga talabalar qo'shish'''
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    def get_students(self):
        '''Har bir talaba haqida ma\'lumot chop etadigan metod'''
        return [talaba.get_info() for talaba in self.talabalar]
#Classlardan obyekt yaratish
matematika = Fan("Oliy matematika")
talaba1 = Talaba("Azizbek", "Jabborov", 2006)
talaba2 = Talaba("Sardor", "Tolliboyev", 2005)
talaba3 = Talaba("Ulug'bek", "Ravshanov", 2000)

#Talabalarni yangi fanga qo'shamiz
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar_soni)
print(matematika.talabalar)

mat_talabalar = matematika.get_students()
print(mat_talabalar)
