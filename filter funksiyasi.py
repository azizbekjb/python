#filter funksiyasi
import random as r
sonlar = r.sample(range(100), 10)
def juftmi(x):
    '''Agar x juft bo'lsa'''
    return x % 2 == 0
juft_sonlar = list(filter(juftmi, sonlar))
print(f"100ta sonda tavakkaliga olingan 10 ta sonlar: {sonlar}")
print(f"100ta sonda tavakkaliga olingan 10 ta sonlar orasidan juft sonlari: {juft_sonlar}")
#Natija:
    # 100ta sonda tavakkaliga olingan 10 ta sonlar: [76, 37, 67, 51, 47, 98, 34, 61, 44, 36]
    # 100ta sonda tavakkaliga olingan 10 ta sonlar orasidan juft sonlari: [76, 98, 34, 44, 36]
