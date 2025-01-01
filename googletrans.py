#12.2: Tashqi kutubxonalar
#googletrans
from googletrans import Translator
tarjimon = Translator()
#Translator - bu maxsus sinf(klass), tarjimon esa obyekt
matn_uz = "Python - dunyodagi eng mashhur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(f"Inglizcha: {tarjima.text}")

#Tarjima tilini o'zgartirish
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(f"Ruscha: {tarjima_ru.text}")

#Ingliz tilidan boshqa tilga
matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
#Matn tilini alohida ko'rsatish
tarjima_uz = tarjimon.translate(matn_en, src='en', dest='uz')
print(f"O'zbekcha: {tarjima_uz.text}")
#Natija:
    # Inglizcha: Python is the most popular programming language in the world
    # Ruscha: Python — самый популярный язык программирования в мире
    # O'zbekcha: Toshkent Oʻzbekistonning poytaxti
