#ro'yxatlar mavzusi:ro'yxatning istalgan joyiga element qo'shish
my_list = [1,2,4]
my_list.insert(2,3)#Bu yerda ro'yxatning 3 - elementining o'riniga 3 qiymatini joylashtiradi'''
print(my_list)  # [1, 2, 3, 4]
#   1-masala
ismlar = ['Azizbek','Sardor','Samar']
#   2-masala
print(f"Salom {ismlar[0]} ishlaring yaxshimi")
print(f"Ko'rinmay ketding {ismlar[1]}")
print(f"Qashqadaryo tinchmi {ismlar[2]}")
#   3-masala
sonlar = []
sonlar.extend([1,2.2,-2])
print(sonlar)
#   4-masala
#1-amal:Ro'yxat elementlarini ko'shish
print(sonlar[0]+sonlar[1])
#2-amal:Ro'yxat elementlarini o'zgartirish
sonlar[2] = 3
#3-amal:Ro'yxat elemntlarini almashtirish.1- va 2-elentlarini o'rnini almashtirish
a = sonlar[0]
sonlar[0] = sonlar[1]
sonlar[1] = a
print(sonlar)
#   5-masala
t_shaxslar = ["Payg'ambarimiz Muhammad S.A.V.","Imom Buxoriy"]
z_shaxslar = ["Ilon Mask","Mark Sukerberg"]
#   6-masala
print(f"Men tarixiy shaxlardan,{t_shaxslar.pop(0)} bilan,\nzamonaviy shaxslardan esa {z_shaxslar.pop(0)}\nbilan suhbat qilishni istar edim")
#   7-masala:
friends = []
friends.append("Sardor")
friends.append("Samar")
friends.append("Adash")
friends.append("Odiljon")
friends.append("Karimjon")
#   8-masala
friends.remove("Sardor")
print(friends)
#   9-masala
friends.insert(0,"Suhrob")
friends.insert(3,"Firdavs")
friends.append("Furqat")
print(friends)
#   10-masala
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print("Mehmonga kelganlar:",mehmonlar)