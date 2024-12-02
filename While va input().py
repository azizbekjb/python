sonlar = list(range(1,11))  #1,...,10
for son in sonlar:
    if son == 5:    #agar son 5ga teng bo'lsa, sikl boshiga qaytaradi
        continue
    print(f"{son} ning kvadrati: {son**2}")
#Natija:
    # 1 ning kvadrati: 1
    # 2 ning kvadrati: 4
    # 3 ning kvadrati: 9
    # 4 ning kvadrati: 16
    # 6 ning kvadrati: 36
    # 7 ning kvadrati: 49
    # 8 ning kvadrati: 64
    # 9 ning kvadrati: 81
    # 10 ning kvadrati: 100