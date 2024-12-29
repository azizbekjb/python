#Fayllar bilan ishlash
#Faylga ma'lumot yozish
filename = 'uztozlar.txt' #Yangi ochilayotgan fayl nomi
with open(filename, 'w') as file:
    file.write("Hello world") #Yangi faylga yozilayotgan matn

#Faylga ma'lumot yozayotgan ma'lumot turi str tipida(matn tipida) bo'lishi kerak

filename = 'new_file.txt'
ism = 'Azizbek Jabborov'
tyil = 2006
with open(filename, 'w') as file:
    file.write(ism + '\n')
    file.write(str(tyil) + '\n')
    #'\n' matnlarni faylda yonma - yon joylashtirmaslik uchun

#Natija:
    #Process finished with exit code 0   
