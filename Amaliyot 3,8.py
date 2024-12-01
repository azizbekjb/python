#   1-masala
davlatlar = ["O'zbekiston","Tojikiston","Qorg'iziston","Qozog'iston"]
print("Asl ro'yxat:",davlatlar)
#1.1-
print("Qator uzunligi:",len(davlatlar))
#1.2-
print("Tartiblangan ro'yxat (sorted()) metodi yordamida:",sorted(davlatlar))
#1.3-
print("Teskari tartiblangan ro'yxat (sorted(davlatlar,reverse=True)) metodi yordamida:",sorted(davlatlar,reverse=True))
#1.4-
print("Asl ro'yxat:",davlatlar)
#1.5-masala
davlatlar.reverse()
print("Ro'yxatni teskari tartiblash:",davlatlar)
#1.6-masala
davlatlar.sort()
print("Ro'yxatni alifbo bo'yicha tartiblash:",davlatlar)
davlatlar.sort(reverse=True)
print("Ro'yxatni alifbo bo'yicha teskari tartiblash:",davlatlar)
#   2-masala
_120_dan_1200_gacha_juft_sonlar = list(range(120,1202,2))
#2.1-masala
print("Ro'yxat yig'indisi:",sum(_120_dan_1200_gacha_juft_sonlar))
#2.2-masala
print("Ro'yxatning eng katta va eng kichik elementlari ayirmasi",max(_120_dan_1200_gacha_juft_sonlar)-min(_120_dan_1200_gacha_juft_sonlar))
#2.3-masala
print("Ro'yxat elementlari soni:",len(_120_dan_1200_gacha_juft_sonlar))
#2.4-masala
print("Ro'yxatning boshidan 20 ta elementni chop etish:",_120_dan_1200_gacha_juft_sonlar[0:20],\
      ".Ro'yxatning o'rtasidandan 20 ta elementni chop etish:",_120_dan_1200_gacha_juft_sonlar[220:240],
      "Ro'yxatning oxiridan 20 elementni chop etish:",_120_dan_1200_gacha_juft_sonlar[-20:])