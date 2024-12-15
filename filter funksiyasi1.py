#filter funksiyasi
mevalar = ["anor", "o'rik", "olma", 'qovun', 'banan']
mevaB = list(filter(lambda meva : meva.startswith('b'), mevalar))
print(f"b harfidan boshlanadigan: {mevaB}")

mevalar2 = list(filter(lambda meva : len(meva) <= 4, mevalar))
print(f"O'lchovi 4 dan kichik  mevalar: {mevalar2}")
#Natija:
    # b harfidan boshlanadigan: ['banan']
    # O'lchovi 4 dan kichik  mevalar: ['anor', 'olma']
