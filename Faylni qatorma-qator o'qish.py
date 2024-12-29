#Fayllar bilan ishlash
#Faylni qatorma-qator o'qish
filename = 'talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line.rstrip())
#Natija:
    # Ali Valiyev
    # Azizbek Jabborov
    # Sardor Tolliboyev

#Qatorlarni ro'yxat ko'risnishida saqlash
with open(filename) as file:
    talabalar = file.readlines()
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)
#rstrip() bo'shliqlarni yo'qotish uchun
#Natija:
    #['Ali Valiyev', 'Azizbek Jabborov', 'Sardor Tolliboyev']
