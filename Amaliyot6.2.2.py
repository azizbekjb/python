#Amaliyot 6.2.2
e_bozor_mahsulotlar= {}
ishora = True

while ishora:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
    e_bozor_mahsulotlar[mahsulot] = narx
    ishora = input(f"(Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if ishora == "yo'q":
        break
    else:
        continue
print(f"Mahsulotlar ro'yxati:")
for mahsulot, narx in  e_bozor_mahsulotlar.items():
    print(f"{mahsulot.title()}ning narxi {narx}$")
#Natija:
    # Mahsulot nomini kiriting: Dell
    # Dellning narxini kiriting: 420
    # (Yana mahsulot qo'shasizmi?(ha/yo'q)ha
    # Mahsulot nomini kiriting: Acer
    # Acerning narxini kiriting: 450
    # (Yana mahsulot qo'shasizmi?(ha/yo'q)ha
    # Mahsulot nomini kiriting: hp
    # Hpning narxini kiriting: 345
    # (Yana mahsulot qo'shasizmi?(ha/yo'q)yo'q
    # Mahsulotlar ro'yxati:
    # Dellning narxi 420$
    # Acerning narxi 450$
    # Hpning narxi 345$
    # 
    # Process finished with exit code 0
