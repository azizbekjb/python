#Amaliyot 8.2.1
def yosh_hisobla(ism, t_yil):
    print(f"{ism.title()} siz {2024 - t_yil} yoshdasiz")
f_ism, f_yosh = map(str, input(f"Ismingiz va tug'ilgan yilingini kiriting: ").split())
yosh_hisobla(f_ism,int(f_yosh))
