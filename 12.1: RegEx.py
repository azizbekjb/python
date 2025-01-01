#12.1: RegEx - Andoza yordamida math izlash
import re
#re - regular expressions
word1 = "temir"
word2 = "tomir"
word3 = "tulpor"
andoza = "^t...r" #5 ta harfdan iborat va boshi t va oxiri r bilan tugaydigan so'zlarni topish
#so'zlarni andozaga solish re.match

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

matn = """Maqolalar 2020-yilning 20-martiga qadar rtmkonferensiya2021@gmail.ru elektron pochtasida qabul qilinadi
    Quyidagi yo'nalishdagi maqalolar qabul qilinadi:
        Aniq va tabiiy fanlarni zamonoviy pedagogik texnologiyalar asosida o'qitish metodikasi.
         Umumta'lim fanlarini o'qitishda STEAM yondashuvining o'rni va ahamiyati. """

#Matnda e-mail ni ajaratib olish andozasi: re.findall()
andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
email = re.findall(andoza, matn)
print(email)

#Kuchli parolni tekshirish
#Ushbu dasturgai barcha andozalar 'ihateregex.io' sahifasidan olindi

andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
msg = "Yangi parol kiriting"
msg += "(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
msg += "1 ta son va 1 ta maxsus belgi boʻlishi kerak): "

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")
#Natija:
    # <re.Match object; span=(0, 5), match='temir'>
    # <re.Match object; span=(0, 5), match='tomir'>
    # None
    # ['rtmkonferensiya2021@gmail.ru']
    # Yangi parol kiriting(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, 1 ta son va 1 ta maxsus belgi boʻlishi kerak): Aziz@121
    # Maxfiy so'z qabul qilindi
