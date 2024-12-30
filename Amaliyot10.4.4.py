#Amaliyot10.4.4
#5
import json
filename = 'C:\\Users\\User\\Downloads\\api-result.json'
with open(filename) as file:
    data = json.load(file)
print(type(data))
print(data["query"]["pages"]["13801"]["title"])
print(data["query"]["pages"]["13801"]["extract"])
#Natija:
    # <class 'dict'>
    # Python
    # Python ([ˈpʌɪθ (ə)n] — payton, piton) — turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning oʻqilishiga urgʻu beradi. Uning til konstruksiyalari va obyektga yoʻnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan. Shuningdek Python sunʼiy intellekt hamda maʼlumotlar muhandisiligi sohalarining tili hisoblanadi.
    # Python deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud boʻlib, uning nomi — IronPython dasturlash muhitidir.
    # Guido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga eʼlon qildi.
    # Python dasturlash tiliga boʻlgan talab yildan yilga oshib bormoqda. CodingDojo portalining tadqiqotlariga koʻra, 2020—2021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng koʻp talab boʻlgan.
