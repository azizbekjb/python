#12.2: Tashqi kutubxonalar
#BeautifulSoup4
import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)


soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-lenta__big l-item") # yangiliklarning mavzusini ajratib olamiz
if len(news) == 0:
    print("Saytga ulanishda xatolik")
else:
    print(news[0].text.strip()) # eng birinchi yangilikni konsolga chiqaramiz
    # Jahon | 18:05 / 30.12.2024
    # Navalniy, G‘azo, «Krokus», Suriya va boshqalar - 2024 yil fotosuratlarda
