#Moslashuvchi funksiya: **kwargs
#Bu yerda kwargs - keyword arguments
def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at
    shklda qaytaradigan dastur"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar
avto1 = avto_info('GM', 'Gentra', rang = 'qora', yil = 2019)
print(avto1)
avto2 = avto_info('GM', 'Malibu', narx = 30000, yil = 2024, rang = 'OQ')
print(avto2)
#Natija:
    # {'rang': 'qora', 'yil': 2019, 'kompaniya': 'GM', 'model': 'Gentra'}
    # {'narx': 30000, 'yil': 2024, 'rang': 'OQ', 'kompaniya': 'GM', 'model': 'Malibu'}
