#Amaliyot7.3.2
ishora = True
while ishora:
    x = int(input("son kiriting: "))
    y = int(input("yana bir son kiriting: "))
    try:
        print(x/y)
        break
    except ZeroDivisionError:
        continue
#Natija:Xato qiymat kiritilganda ishlaydigan dastur.To'g'ri qiymatda bir marta ishlaydi
    # son kiriting: 2
    # yana bir son kiriting: 0
    # son kiriting: 3
    # yana bir son kiriting: 0
    # son kiriting: 3
    # yana bir son kiriting: 1
    # 3.0
