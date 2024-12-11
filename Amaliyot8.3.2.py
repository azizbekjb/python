#Amaliyot8.3.2
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
mijozlar = []
print("Mijozlar ro'yxatini tuzamiz: ")
while True:
    ismi = input('Mijozning ismini kiriting: ')
    familiyasi = input('Mijozning familiyasini kiriting: ')
    t_yili = input("Mijozning tug'ilgan yilini kiriting: ")
    t_joyi = input("Mijozning tug'ilgan joyini kiriting: ")
    e_manzili = input("Mijozning electron manzilini kiriting(majburuiy emas): ")
    tel_raqami = input('Mijozning telefon raqamini kiriting(majburiy emas): ')
    mijozlar.append(malumot(ismi, familiyasi, t_yili, t_joyi, e_manzili, tel_raqami))
    javob = input("Yana ma'lumot qo'shasizmi?(ha/yo'q)")
    if javob == "yo'q":
        break
print("Mijozlar haqida:")
for mijoz in mijozlar:
    if mijoz['e_manzili']:
        e_manzil = mijoz['e_manzili']
    else:
        e_manzil = "Nomalum"
    if mijoz['tel_raqami']:
        tel_raqam = mijoz['tel_raqami']
    else:
        tel_raqam = "Nomalum"
    print(f"Mijozning ismi: {mijoz['ismi']}\n"
          f"Mijoz familiyasi: {mijoz['familiyasi']}\n"
          f"Mijozning tug'ilgan yili: {mijoz['t_yili']}\n"
          f"Mijozning manzili: {mijoz['t_joyi']}\n"
          f"Mijozning electron pochtasi: {e_manzil}\n"
          f"Mijoznig telefon raqami: {tel_raqam}")
#Natija:
    # Mijozlar ro'yxatini tuzamiz:
    # Mijozning ismini kiriting: Azizbek
    # Mijozning familiyasini kiriting: Jabborov
    # Mijozning tug'ilgan yilini kiriting: 2006
    # Mijozning tug'ilgan joyini kiriting: Samarkand
    # Mijozning electron manzilini kiriting(majburuiy emas):
    # Mijozning telefon raqamini kiriting(majburiy emas):
    # Yana ma'lumot qo'shasizmi?(ha/yo'q)ha
    # Mijozning ismini kiriting: Sardor
    # Mijozning familiyasini kiriting: Tolliboyev
    # Mijozning tug'ilgan yilini kiriting: 2005
    # Mijozning tug'ilgan joyini kiriting: Samarkand
    # Mijozning electron manzilini kiriting(majburuiy emas):
    # Mijozning telefon raqamini kiriting(majburiy emas):
    # Yana ma'lumot qo'shasizmi?(ha/yo'q)yo'q
    # Mijozlar haqida:
    # Mijozning ismi: Azizbek
    # Mijoz familiyasi: Jabborov
    # Mijozning tug'ilgan yili: 2006
    # Mijozning manzili: Samarkand
    # Mijozning electron pochtasi: Nomalum
    # Mijoznig telefon raqami: Nomalum
    # Mijozning ismi: Sardor
    # Mijoz familiyasi: Tolliboyev
    # Mijozning tug'ilgan yili: 2005
    # Mijozning manzili: Samarkand
    # Mijozning electron pochtasi: Nomalum
    # Mijoznig telefon raqami: Nomalum
