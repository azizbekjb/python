#Fayllar bilan ishlash
#Fayladan ma'lumot olish
with open('pi.txt') as file:
    pi = file.read()
print(pi)
#Natija:
    # 3.1415926535
    # 8979323846
    # 2643383279

#1 qator oxiridagi bo'shliqlarni o'chirish
pi = pi.rstrip()
#2 qator tashlash belgisini almashtiramiz
pi = pi.replace('\n','')
#3 matnni float(o'nlik) songa o'tkazamiz
pi = float(pi)
print(pi)
#Natija:
    # 3.141592653589793

#Papka ichidagi fallarni ochish
#filename = 'C:\\Dasturlar\\pi.txt'
