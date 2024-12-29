#Fayllar bilan ishlash
#pickle faylga yozish va unda ma'lumotlarni o'qish
#yozish: 'wb' - write binary
#o'qish: 'rb' - read binary
#yozish uchun pickle.dump()
#o'qish uchun pickle.load()
import pickle
talaba1 = {
    'ism' : 'Azizbek',
    'familiya' : 'Jabborov',
    'tyil' : 2006,
    'kurs' : 2
}
talaba2 = {
    'ism' : 'Sardor',
    'familya' : 'Tolliboyev',
    'tyil' : 2005,
    'kurs' : 2
}
#pickle faylga yozish
with open('info', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)

#pickle fayldan o'qish
with open('info', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
print(talaba1)
#Natija:
    #{'ism': 'Azizbek', 'familiya': 'Jabborov', 'tyil': 2006, 'kurs': 2} 
print(talaba2)
    #{'ism': 'Sardor', 'familya': 'Tolliboyev', 'tyil': 2005, 'kurs': 2}
