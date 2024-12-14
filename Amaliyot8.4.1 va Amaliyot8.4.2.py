#Amaliyot8.4.1 va Amaliyot8.4.2
def bosh_harf(ismlar):
    katta_harflar = []
    for i in ismlar:
        katta_harflar.append(i.capitalize())
    return katta_harflar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bosh_harf(talabalar[:])
print(f"Ismlar bosh harfga o'zgartirildi: {baholar}")
#Natija:
    #Ismlar bosh harfga o'zgartirildi: ['Ali', 'Vali', 'Hasan', 'Husan']
