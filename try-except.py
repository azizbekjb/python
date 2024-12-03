#7.2. exceptions(istisnolar)
#Xatoni tutib olish
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh) # xato qaytargan qator
    print(f"Siz {2024 - yosh} yilda tug'ilgansiz")
except:#Xato yuz berganda bajariluvchi kod
    print("Butun son kiritmadingiz!")
print("Dastur tugadi!")
#Natija:
    #1-shart:
        # Yoshingizni kiriting: 17
        # Siz 2007 yilda tug'ilgansiz
        # Dastur tugadi!
    #2-shart
        # Yoshingizni kiriting: 43.9
        # Butun son kiritmadingiz!
        # Dastur tugadi!
