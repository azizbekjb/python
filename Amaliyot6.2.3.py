#Amaliyot 6.2.3
buyurtma_mahsulotlar = []
e_bozor_mahsulotlar= {
    "dell" : 450,
    "lenovo" : 340,
    "acer" : 330,
    "macbook" : 1000,
    "hp" : 500,
    "asus" : 455
}
ishora = True
print("Qaysi mahsulotlar kerak?")
while ishora:
    mahsulot = input("Mahsulot nomini kiriting: ")
    buyurtma_mahsulotlar.append(mahsulot)
    if mahsulot.lower() in e_bozor_mahsulotlar.keys():
        print(f"{mahsulot.title()}ning narxi: {e_bozor_mahsulotlar[mahsulot]}")
    else:
        print("Bizda bu mahsulot yo'q")
    ishora = input(f"(Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if ishora == "yo'q":
        break
    else:
        continue
#Natija:
    # Qaysi mahsulotlar kerak?
    # Mahsulot nomini kiriting: dell
    # Dellning narxi: 450
    # (Yana mahsulot qo'shasizmi?(ha/yo'q)ha
    # Mahsulot nomini kiriting: lenovo
    # Lenovoning narxi: 340
    # (Yana mahsulot qo'shasizmi?(ha/yo'q)ha
    # Mahsulot nomini kiriting: vostro
    # Bizda bu mahsulot yo'q
    # (Yana mahsulot qo'shasizmi?(ha/yo'q)yo'q
