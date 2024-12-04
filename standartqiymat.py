#Standart qiymat
def yosh_hisobla(tugilgan_yil, joriy_yil = 2024):
    print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
n = int(input("Yoshingizni kiriting:"))
yosh_hisobla(n) #2- kiritmagan hol
yosh_hisobla(n, 2023) ##2- argument kiritgan hol
#Natija:
    #Yoshingizni kiriting:2006
    #1-shart
        #Siz 18 yoshdasiz
    #2-shart:
        #Siz 17 yoshdasiz
