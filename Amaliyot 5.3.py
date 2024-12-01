#   1-masala:
ranglar = {'qizil','sariq','oq'}
#   1-masala tamom

#   2-masala:
ranglar.add('yashil')
ranglar.update({'ko\'k', 'Binafsha'})
print(ranglar)
#   2-masala tamom

#   3-masala
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = sorted(set1.union(set2))
print(set3)
#   3-masala tamom

#   4 - masala:
print(set1.difference(set2))
#   4-masala tamom

#   5-masala:
print(set1.symmetric_difference(set2))
#   5-masala tamom

#   9,10-masala
bozorlik = ['choy','non', 'kartoshka', 'tuxum', 'sut']
mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
bor_mahsulotlar = []
yoq_mahsulotlar = []
for mahsulot in bozorlik:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    elif mahsulot not in mahsulotlar:
        yoq_mahsulotlar.append(mahsulot)
print(bor_mahsulotlar)
print(yoq_mahsulotlar)