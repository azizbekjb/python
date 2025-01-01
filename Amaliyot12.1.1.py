#Amaliyot12.1
#1, 2, 3
from datetime import*
def yosh(t_sana):
    bugun = datetime.today()
    farq = bugun - t_sana
    yillar = farq.days // 365
    oylar = (farq.days % 365) // 30
    kunlar = (farq.days % 365) % 30

    return (f"Tug'ilgan kuningizdan bugungi kungacha: {yillar} yil, {oylar} oy, {kunlar} kun o'tdi.")
#1
bugun = datetime.now()
print("10 ta sana:")
for i in range(10):
    print(bugun.date())
    bugun = bugun - timedelta(days=14)

#2
bugun = datetime.today()
ramazon_hayit = datetime(2025, 3, 31)
qurbon_hayit = datetime(2025, 6, 7)
ramazon_qoldiq = ramazon_hayit - bugun
qurbon_qoldiq = qurbon_hayit - bugun
print(f"Ramazon hayit bayramiga {(ramazon_qoldiq).days} kun qoldi")
print(f"Qurbon hayit bayramiga {(qurbon_qoldiq).days} kun qoldi")

#3
my_birtday = datetime(2006, 3, 13)
print(yosh(my_birtday))
#Natija:
    # 10 ta sana:
    # 2025-01-01
    # 2024-12-18
    # 2024-12-04
    # 2024-11-20
    # 2024-11-06
    # 2024-10-23
    # 2024-10-09
    # 2024-09-25
    # 2024-09-11
    # 2024-08-28
    # Ramazon hayit bayramiga 88 kun qoldi
    # Qurbon hayit bayramiga 156 kun qoldi
    # Tug'ilgan kuningizdan bugungi kungacha: 18 yil, 9 oy, 29 kun o'tdi.
