#   1)
my_set = {1,2,3}
print(my_set)
my_set = {1,1,1,3,3,3,54,53,3,2,2}
print(my_set)

#   2)Bo'sh to'plam yaratish
my_set = set()  #bo'sh to'plam

#   3)To'plamga indeks orqali murojaat qilish.Ularga indeks orqali murojaat qilib bo'lmaydi
sonlar = {1,2,3,3,12}
#print(sonlar[0])   #TypeError: 'set' object is not subscriptable

#   4)Ro'yxatdan to'plamga o'tish
sonlar = [1,2,3,2,2,2,4,1,2,3,4,31,3]
sonlar = set(sonlar)
print(f"Hosil bo'lgan to'plam:{sonlar}")

#   5)To'plamdan ro'yxatga o'tish
sonlar = list(sonlar)
print(f"Hosil bo'lgan ro'yxat:{sonlar}")

#   6)To'plamga yagona element qo'shish->.add() metodi
raqamalar = {1,2,3,4,5}
print(f"Oldingi to'plam {raqamalar}")
raqamalar.add(7)
print(f"Yangi to'plam {raqamalar}")

#   7)To'plamga bir nechta element qo'shish->.update() metodi
print(f"Oldingi to'plam {raqamalar}")   #Oldingi to'plam {1, 2, 3, 4, 5, 7}
raqamalar.update({6,8,9})
print(f"Yangi to'plam {raqamalar}") #Yangi to'plam {1, 2, 3, 4, 5, 6, 7, 8, 9}

#   8.1)To'plam elementini o'chirish->.discard() metodi
print(f"Oldingi to'plam {raqamalar}") #Oldingi to'plam {1, 2, 3, 4, 5, 6, 7, 8, 9}
raqamalar.discard(2)
print(f"Yangi to'plam {raqamalar}") #Yangi to'plam {1, 3, 4, 5, 6, 7, 8, 9}

#   8.2)To'plam elementini o'chirish->.remove() metodi
print(f"Oldingi to'plam {raqamalar}") #Oldingi to'plam {1, 3, 4, 5, 6, 7, 8, 9}
raqamalar.remove(1)
print(f"Yangi to'plam {raqamalar}") #Yangi to'plam {3, 4, 5, 6, 7, 8, 9}
# Bu ikki metodning farqi agar siz to'plamda yo'q elementni o'chirmoqchi bo'lsangiz ".remove()" metodi xato qaytaradi,".discard()" metodi esa unday emas

#   8.3)To'plam elementini o'chirish->.pop() metodi
#Lekin pop metodi indeks bo'yicha ishlaganligi sababli tasodifiy elemntni sug'urib oladi
raqam = raqamalar.pop()
print(f"Kesib olingan raqam {raqam}")
print(f"Yangi to'plam {raqamalar}")