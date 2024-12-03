# Ro'yxatdan ro'yxatga element qo'shish
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()# elementni sug'urib olish
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
#Natija:
    # Botirning bahosini kiriting: 5
    # Botir baholandi
    # Olimning bahosini kiriting: 4
    # Olim baholandi
    # Husanning bahosini kiriting: 3
    # Husan baholandi
    # Hasanning bahosini kiriting: 3
    # Hasan baholandi
    # 
    # Process finished with exit code 0
