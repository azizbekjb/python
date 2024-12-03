#   While yordamida ro'yxatni to'ldirish
ismlar = [] # ismalar ro'yxati
print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n = 1#  ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n} - do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi(ha/yo'q)")
    if javob == "ha":
        n += 1
        continue
    else:
        break
print("Ro'yxat tuzildi")
#Natija:
    # Yaqin do'stlaringiz ro'yxatini tuzamiz.
    # 1 - do'stingiz ismini kiriting: Azizbek
    # Yana ism qo'shasizmi(ha/yo'q)ha
    # 2 - do'stingiz ismini kiriting: Sardor
    # Yana ism qo'shasizmi(ha/yo'q)yo'q
    # Ro'yxat tuzildi
