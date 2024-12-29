#Amaliyot10.3
#4
filename = 'userfile.txt'
with open(filename, 'a') as file:
    ism = input('Ismingizni kiriting: ')
    familiya = input('Familiyangizni kiriting: ')
    yosh = input('Yoshingizni kiriting: ')
    file.write(ism + '\n')
    file.write(familiya + '\n')
    file.write(yosh + '\n')
#Fayldan o'qish.Tekshirish
with open(filename) as file:
    for line in file:
        print(line.rstrip())
#Natija:
    # Ismingizni kiriting: Azizbek
    # Familiyangizni kiriting: Jabborov
    # Yoshingizni kiriting: 18
    # Azizbek
    # Jabborov
    # 18
