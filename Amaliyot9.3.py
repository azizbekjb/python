#Amaliyot9.3
class User:
    def __init__(self, f_ism, ism, familiya, yosh, e_mail):
        self.ismi = ism
        self.familiyasi = familiya
        self.yoshi = yosh
        self.foydalanuvchi_ismi = f_ism
        self.e_mail = e_mail
    def get_info(self):
        print(f"Foydalanuvchi {self.foydalanuvchi_ismi}. Ismi: {self.ismi} {self.familiyasi}.\n"
              f"Yoshi: {self.yoshi} da\n"
              f"email: {self.e_mail}. ")
user1 = User('Azizbek123', 'Azizbek', 'Jabborov', 18, 'ajabborov1212121@gmail.com')
user1.get_info()
#Natija:
    # Foydalanuvchi Azizbek123. Ismi: Azizbek Jabborov.
    # Yoshi: 18 da
    # email: ajabborov1212121@gmail.com. 
