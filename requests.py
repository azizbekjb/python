#12.2: Tashqi kutubxonalar
#requests
import requests
from pprint import pprint
manzil = "https://kun.uz/news/main"
r = requests.get(manzil)
# pprint(r.text)
#Natija:
    #Bu koda natijasi juda uzun.Shu sabali izohga olindi

# restcountries.eu - davlatlar haqida ma'lumot beruvchi sayt
#Pasta xatolik bor
# country = "Uzbekistan"
# api_key = "API_KEY"  # Haqiqiy API kalitingizni yozing
# url = f"https://api.countrylayer.com/v2/name/{country}?access_key={api_key}"
#
# response = requests.get(url)
#
# if response.status_code == 200:  # So'rov muvaffaqiyatli bo'lsa
#     r_json = response.json()[0]
#     print(r_json['capital'])
# else:
#     print("Saytga ulanishda xatolik yoki noto'g'ri API kaliti")
