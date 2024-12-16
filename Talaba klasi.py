#Talaba klasi
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

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning to'liq ism-familyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
        # Argument qabul qiluvchi metod

    def get_age(self, yil):
        """Talabaning yoshini qaytardi"""
        return yil - self.t_yil
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
talaba1 = Talaba('Azizbek', 'Jabborov', 2006)
#Obyektning metodlarini lug'at ko'rishda cho etish
print(talaba1.__dict__)
print("Kerakli metodlar")
print(see_methods(Talaba))
print("Klass metodlari")
for metod in dir(Talaba):
    print(metod)
#Natija:
    #{'ism': 'Azizbek', 'familiya': 'Jabborov', 't_yil': 2006, 'bosqich': 1}
    # Kerakli metodlar
    # ['get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'set_bosqich', 'update_bosqich']
    # Klass metodlari
    # __class__
    # __delattr__
    # __dict__
    # __dir__
    # __doc__
    # __eq__
    # __format__
    # __ge__
    # __getattribute__
    # __getstate__
    # __gt__
    # __hash__
    # __init__
    # __init_subclass__
    # __le__
    # __lt__
    # __module__
    # __ne__
    # __new__
    # __reduce__
    # __reduce_ex__
    # __repr__
    # __setattr__
    # __sizeof__
    # __str__
    # __subclasshook__
    # __weakref__
    # get_age
    # get_fullname
    # get_info
    # get_lastname
    # get_name
    # set_bosqich
    # update_bosqich
