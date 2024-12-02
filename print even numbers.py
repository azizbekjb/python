#Juft sonlarni continue operatori orqali chiqarish
#print even numbers using the "continue" operator
sonlar = list(range(1,11))  #1,...,10
for son in sonlar:
    if son % 2 != 0:    #agar son toq bo'lsa, sikl boshiga qaytaradi
        continue
    print(son, end=' ')
#Natija:
    #2 4 6 8 10 
