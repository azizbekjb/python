#Amaliyot7.3.2
ishora = True
while ishora:
    x = int(input("son kiriting: "))
    y = int(input("yana bir son kiriting: "))
    try:
        print(x, '/', y, '=', x / y)
    except ZeroDivisionError:
        print("nol kiritmang")
        continue
