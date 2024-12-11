#Amaliyot8.3.1
def malumot(ismi, familiyasi, t_yili, t_joyi, e_mazil = '', tel_raqami = ''):
    h_malumot = {
        'ismi': ismi,
        'familiyasi' : familiyasi,
        't_yili' : t_yili,
        't_joyi' : t_joyi,
        'e_manzili' : e_mazil,
        'tel_raqami' : tel_raqami
    }
    return h_malumot
ismi = input('Ismingizni kiriting: ')
familiyasi = input('Familiyangizni kiriting: ')
t_yili = input("Tug'ilgan yilingizni kiriting: ")
t_joyi = input("Tug'ilgan joyingizni kiriting: ")
e_manzili = input("Electron manzilingizni kiriting(majburuiy emas): ")
tel_raqami = input('Telefon raqamingizni kiriting(majburiy emas): ')
print("Siz haqingizda to'liq ma'lumot:")
print(malumot(ismi, familiyasi, t_yili, t_joyi, e_manzili, tel_raqami))
#Natija:
    # Ismingizni kiriting: Azizbek
    # Familiyangizni kiriting: Jabborov
    # Tug'ilgan yilingizni kiriting: 2006
    # Tug'ilgan joyingizni kiriting: Samarqand
    # Electron manzilingizni kiriting(majburuiy emas): 
    # Telefon raqamingizni kiriting(majburiy emas): 
    # Siz haqingizda to'liq ma'lumot:
    # {'ismi': 'Azizbek', 'familiyasi': 'Jabborov', 't_yili': '2006', 't_joyi': 'Samarqand', 'e_manzili': '', 'tel_raqami': ''}
    # 
    # Process finished with exit code 0
