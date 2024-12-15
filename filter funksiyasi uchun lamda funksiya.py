#filter funksiyasi uchun lamda funksiya
import random as r
sonlar = r.sample(range(100), 10)
juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(f"100ta sonda tavakkaliga olingan 10 ta sonlar: {sonlar}")
print(f"100ta sonda tavakkaliga olingan 10 ta sonlar orasidan juft sonlari: {juft_sonlar}")
#Natija:
    # 100ta sonda tavakkaliga olingan 10 ta sonlar: [84, 29, 90, 96, 20, 44, 21, 12, 81, 3]
    # 100ta sonda tavakkaliga olingan 10 ta sonlar orasidan juft sonlari: [84, 90, 96, 20, 44, 12]
