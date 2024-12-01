#   1-masala:
Python = {
    'int' : 'Integer',
    'float' : 'float',
    'str' : 'string',
    'bool' : 'boolean',
    'char' : 'charactive',
}
for kalit,qiymat in sorted(Python.items()):
    print(f"{kalit} -> {qiymat}")
#   1-masala tugadi

#   2-masala:
Davlatlar_poytaxtlar = {
    'O\'zbekiston' : 'Toshkent',
    'Rossiya' : 'Moskva',
    'AQSH' : 'Vashington',
    'Fransiya' : 'Parij',
    'italiya' : 'rim',
    'germaniya' : 'berlin',
    'ispaniya' : 'madrid'
}
for davat in sorted(Davlatlar_poytaxtlar.keys()):
    print(davat.capitalize())
for poytaxt in sorted(Davlatlar_poytaxtlar.values()):
    print(poytaxt.capitalize())
#   2-masala tugadi

#   3-masala:
davlat = input('Hurmatli foydalanuvchi,istalgan davlat nomini kiriting\n>>>')
if davlat in Davlatlar_poytaxtlar:
    print(f"{davlat} poytaxti-> {Davlatlar_poytaxtlar[davlat]}")
else:
    print('Bunday davlat mavjud emas')
#   3-masala tugadi
#   4-masala:
taomalar ={
    'osh' : 25000,
    'manti' : 5000,
    'kabob' : 14000,
    'sho\'rva': 25000,
    'chuchvara' : 20000,
    'do\'lma' : 10000,
    'xot dog' : 11000
}
buyurtma = []
for b in range(3):
    b1 = input(f"{b+1} - taomni kiritng\n->")
    buyurtma.append(b1)
for taom in buyurtma:
    if taom in taomalar:
        print(f"{taom} ning narxi {taomalar[taom]}")
    else:
        print(f"Bizda {taom} yo'q!!!")