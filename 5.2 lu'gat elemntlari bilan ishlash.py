# .items() metodi.Lug'atdagi kalit-qiymat juftligini chiqarish
car = {
    'Name' : "Nissan",
    'model' : 'GTR',
    'Price' : '100000 $'
}
print(car.items())
# Ushbu metodni sikl yordamida hosil qilish
for kalit, qiymat in car.items():
    print(f"{kalit} : {qiymat}")
# .keys() metodi
#   Lug'atdagi kalit so'zlarni chiqarish uchun foydalaniladi
mahsulotlar = {
    'olma' : 20000,
    'anor' : 30000,
    'uzum' : 2341,
    'olcha' : 8992
}
print(mahsulotlar.keys())


#     Ro'yxat va lug'at
bozorlik = ['anor','uzum','olma','olcha']
for m in mahsulotlar:
    if m in bozorlik:
        print(f"{m.title()} {mahsulotlar[m]} so'm")
bozorlik = ['non','baliq','shaftoli','olma']
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Kechirasiz bizda {buyum} yo'q")
    else:
        print(f"Bizda {buyum} bor!")

#       Lug'at elementlarini tartib bilan chaqirish
#1)
print('Do\'kondagi mahsulotlar(tartiblangan holda):')
for mahsulot in sorted(mahsulotlar):
    print(mahsulot)
#2)       .values metodi
print(mahsulotlar.values())
#3)
print('Do\'kondagi mahsulotlar narxlari:')
for mahsulot in mahsulotlar.values():
    print(mahsulot)
#4) .set() metodi,to'plam yasashda qo'llaniladi
telefonlar = {
    'Sardor' : 'Redmi A10',
    'Ulug\'bek' : 'Samsung galaxsy A54',
    'Azizbek' : 'Infinix hot 30i',
    'Komron' : 'Infinix Smart 7',
    'odiljon' : 'Redmi A10',
    'Karimjon' : 'Infinix hot 30i'
}
print('Foydalanuvhchilar telefonlari:')
for tel in set(telefonlar.values()):
    print(tel)
