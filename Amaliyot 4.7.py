'''mahsulotlar = ['sabzi','olma','karam','kartoshka','pomidor','shaftoli','non','uzum','o\'rik','anor']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for i in range(5):
    savatga = input(f"Hurmatli mijoz {i+1}- mahsulotni kiriting:")
    savat.append(savatga)
for mahsulot  in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar bor")
else:
    print("QUYIDAGI MAHSULOT MAVJUD EMAS:",end=' ')
    for m in mavjud_emas:
        print(m, end=' ')'''
foydalanuvhchilar = ['aaab','c1heje','evieiei','veb3vbibr','hbi3rbibibibifj']
foydalanuvhchi = input("Loginni kiriting:")
if foydalanuvhchi in foydalanuvhchilar:
    foydalanuvhchi = input("Login band, qayta kiriting:")
    if foydalanuvhchi not in foydalanuvhchilar:
        print('Xush kelibsiz')
