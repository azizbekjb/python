#8.3:Funksiyani siklda ishlatish
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
print("Avtomobil(lar) haqida:")
for avto in avtolar:
    print(f"Ishlab chiqaruvchi: {avto['kompaniya']}\n"
          f"Modeli: {avto['model']}\n"
          f"Rangi: {avto['rang']}\n"
          f"Ishlab chiqarilgan yili: {avto['yil']}\n"
          f"Narxi: {avto['narx']}")
#Natija:
    # Saytimizdagi avtolar ro'yxatini shakllantiramiz.
    # Quyidagi ma'lumotlarni kiriting:
    # Ishlab chiqaruvchi: GM
    # Modeli: Gentra
    # Rangi: Oq
    # Karobka: Mexanika
    # Ishlab chiqarilgan yili: 2019
    # Narxi: 9100
    # Yana avto qo'shasizmi?(yes/no):no
    # Avtomobil(lar) haqida:
    # Ishlab chiqaruvchi: GM
    # Modeli: Gentra
    # Rangi: Oq
    # Ishlab chiqarilgan yili: 2019
    # Narxi: 9100
