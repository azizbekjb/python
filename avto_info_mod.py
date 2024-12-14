def avto_info(make, model, rangi, korobka, yili, narxi=None):
    avto = {
        'kompaniya' : make,
        'rang' : rangi,
        'model' : model,
        'korobka' : korobka,
        'yil' : yili,
        'narx' : narxi
    }
    return avto
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []
def avto_kirit():
    while True:
        print("Quyidagi ma'lumotlarni kiriting:", end='\n')
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input('Rangi: ')
        korobka  = input("Karobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narxi = input("Narxi: ")
        #Kiritilgan ma'lumotlardan avto_info() yordamida
        #lug'at shakllantirib, ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        javob = input("Yana avto qo'shasizmi?(yes/no):")
        if javob == 'no':
            break
    return avtolar
print("Avtomobil(lar) haqida:")
def info_print():
    for avto in avtolar:
        print(f"Ishlab chiqaruvchi: {avto['kompaniya'].upper()}\n"
              f"Modeli: {avto['model'].upper()}\n"
              f"Rangi: {avto['rang'].upper()}\n"
              f"Ishlab chiqarilgan yili: {avto['yil'].upper()}\n"
              f"Narxi: {avto['narx'].upper()}")