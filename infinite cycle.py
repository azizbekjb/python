son =0
while son < 10:
    if son % 2 != 0:
        continue # Bu yerda yana qaytadi sonni 2 ga bo'lganda qodiq har safar 1 chiqaveradi
    else:
        print(son)# Bir marta nol chop etiladi
    son += 1 # bir marta bir oshiradi
