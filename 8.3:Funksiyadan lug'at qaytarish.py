#8.3:Funksiyadan lug'at qaytarish
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
avto1 = avto_info('GM', "Malibu", 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', "Gentra", 'Oq', 'Avtomat', 2016, 15000)
avtolar = [avto1, avto2]
print("Onlayn bozorda mavjud avtolar:")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")
#Natija:
# Qora Malibu. Narxi: Noma'lum
# Oq Gentra. Narxi: 15000
