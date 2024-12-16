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
