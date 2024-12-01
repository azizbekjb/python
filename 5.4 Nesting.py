car0 = {
    'model' : 'lacetti', 'rang' : 'oq',
    'yil' : 2018, 'narx' : 13000,
    'km' : 50000, 'korobka' : 'avtomat'
}
car1 = {
    'model' : 'nexia 3', 'rang' : 'qora',
    'yil' : 2015, 'narx' : 9000,
    'km' : 89000, 'korobka' : 'mexanika'
}
car2 = {
    'model' : 'gentra', 'rang' : 'qizil',
    'yil' : 2019, 'narx' : 15000,
    'km' : 20000, 'korobka' : 'mexanika'
}
cars = [car0, car1, car2]   #LUG'ATLAR ro'yxati
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['rang']} rang,"
          f"{car['yil']} - yil, {car['narx']}$")
print(cars[0])  # Cars  ro'yxatidagi 1 - lug'atning elementlar juftligi
print(cars[0]['model']) # cars ro'yxatidagi 1 - lug'atning 'model' kalit so'zidagi qiymatni chop etish


#   for sikli yordamida bo'sh lug'at yaratish
malibus=[]   #malibu mashinalari uchun bo'sh ro'yxat
for n in range(10):
    new_car = {#    har bir yangi mashina uchun lug'at yaratamiz
        'model' : "malibu",
        'rang' : None,#     rangi noaniq
        'yil' : 2020,
        'narx' : None,
        'karobka' : "avto"
    }
    malibus.append(new_car)#     lug'atni ro'yxatga qo'shamiz
#   birinchi 3 ta mashinaga 'qizil' rang beramiz
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'
#   keyingi 3tasiga qora
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
#   oxirgi 4 tasini qora,karobkasini mexanika qilamiz
for malibu in malibus[6:]:
    malibu['rang'] = 'qora'
    malibu['karobka'] = 'mexanika'
#   mashinalarning karobkasiga qarab narx belgilaymiz
for malibu in malibus:
    if malibu['karobka'] == 'avto':
        malibu['narx'] = 40000
    else:
        malibu['narx'] = 35000
#   masshinalar ro'yxatini konsolga chiqarish
for malibu in malibus:
    print(malibu.values())

