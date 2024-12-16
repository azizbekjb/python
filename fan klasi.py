class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    def add_student(self, talaba):
        '''Fanga talabalar qo'shish'''
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_nomi(self):
        return self.nomi
    def get_students(self):
        '''Har bir talaba haqida ma\'lumot chop etadigan metod'''
        return [talaba.get_info() for talaba in self.talabalar]
    def get_students_num(self):
        return self.talabalar_soni
print("Klassning metodlari")
for metod in dir(Fan):
    print(metod)
#Natija:
    # Klassning metodlari
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
    # add_student
    # get_nomi
    # get_students
    # get_students_num
