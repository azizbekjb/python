#7.3. Xatolarni oldini olish
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
print(f"Siz {2024 - yosh} yilda tug'ilgansiz")
#Natija:
    # Yoshingizni kiriting: 12.5
    # Yoshingizni kiriting: 23.2
    # Yoshingizni kiriting: 18
    # Siz 2006 yilda tug'ilgansiz
#Izoh:
    #.isdigit(12.5) == false
    #.isdigit(18) == true
