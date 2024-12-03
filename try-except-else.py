#7.2. exceptions(istisnolar)
#try-except-else
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except:#Xato yuz berganda bajariluvchi kod
    print("Butun son kiritmadingiz!")
else:
    print(f"Siz {2024 - yosh} yilda tug'ilgansiz")
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
