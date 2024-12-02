sonlar = list(range(1,11))  #1,...,10
for son in sonlar:
    if son == 5:    #agar son 5ga teng bo'lsa sikl to'xtaydi
        break
    print(f"{son} ning kvadrati: {son**2}")
#Natija:
    # 1 ning kvadrati: 1
    # 2 ning kvadrati: 4
    # 3 ning kvadrati: 9
    # 4 ning kvadrati: 16
