#Amaliyot 6.2.1
mahsulotlar = []
while True:
    mahsulot = input("Mahsulot nomini kiriting(to'xtash uchun 'exit' kiriting): ")
    if mahsulot == 'exit':
        break
    else:
        mahsulotlar.append(mahsulot)
print(f"Mahsulotlar ro'yxati: {mahsulotlar}")
#Natija:
    # Mahsulot nomini kiriting(to'xtash uchun 'exit' kiriting): Lenovo
    # Mahsulot nomini kiriting(to'xtash uchun 'exit' kiriting): Dell
    # Mahsulot nomini kiriting(to'xtash uchun 'exit' kiriting): exit
    # Mahsulotlar ro'yxati: ['Lenovo', 'Dell']
