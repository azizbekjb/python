#   1-masala
ismlar = ["Sardor","Azizbek","Samar","Odil","Suhrob"]
for ism in ismlar:
    print(f"Hurmatli do'stim {ism},sizni 13-mart kuni tug'ilgan kunimga taklif qilaman.")
    print("Hurmat bilan do'stingiz Azizbek")
#   2-masala
print("Kod besh marta takrorlandi")
#   3-masala
_11_dan_100_gacha_toq_sonlar_royxati = list(range(11,100,2))
for son in _11_dan_100_gacha_toq_sonlar_royxati:
    print(son,"ning kubi",son**3)
#   4-masala
print("Hurmatli foydalanuvhchi siz 5 ta eng yaxshi ko'rgan filmraringizni kiritishingiz mumkin!!!")
filmlar = []
for i in range(5):
    film = input(f">>>{i+1}-film:")
    filmlar.append(film)
print("Siz yoqtirgan filmlar TOP 5 taligi:",filmlar)
#   5-masala
son = int(input("Bugun nechat odam bilan subatlashdingiz"))
odamlar = []
for s in range(son):
    odam = input(f"{s+1}-odam:")
    odamlar.append(odam)
print(f"Siz bugun uchrashgan {son} ta odamlar:",odamlar)