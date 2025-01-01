#12.1: datetime - sana va vaqt
import datetime as dt
hozir = dt.datetime.now()
print(hozir)

# Sanani ajratib olish
print(f"Bugungi sana: {hozir.date()}")

# Vaqtni ajratib olish
print(f"Hozirgi vaqt: {hozir.time()}")

#Soatni ajratib olish
print(f"Soat: {hozir.hour}")

# Minutni ajratib olish
print(f"Minut: {hozir.minute}")

# Sekundni ajaratib olish
print(f"Sekund: {hozir.second}")

#Bugungi kunning sanasi
bugun = dt.date.today()
print(f"Bugungi kungi sana: {bugun}")

#Ertangi sana
ertaga = dt.date(2025, 1, 2)
print(f"Ertangi sana: {ertaga}")

#Hozirgi vaqt
vaqtHozir = hozir.time()
print(f"Hozir vaqt: {vaqtHozir}")

#Ayirish operatori
ramazon = dt.date(2025, 3, 1)
farq = ramazon - bugun
print(f"Ramazonga {farq.days} kun qoldi!")

#Yil oy kun soat minut sekund
futbol = dt.datetime(2025, 1, 2, 23, 45, 00)

#Vaqtni ajratib olish
farq = futbol - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(farq)
print(f"Futbol boshlanishiga {sekundlar} s qoldi")
print(f"Futbol boshlanishiga {minutlar} min qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

#Vaqtni millisekundsiz chiqarish
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir vaqt: {vaqt}")

#Sanani kun-oy-yil ko'rinishida chiqarish
sana = hozir.strftime("%d-%m-%y")
print(f"Sana: {sana}")

#Sana vaqtni chiroyli chiqarish
sana_vaqt = hozir.strftime("%d-%m-%y, %H:%M")
print(sana_vaqt)
#Natija:
    # 2025-01-01 15:13:47.328620
    # Bugungi sana: 2025-01-01
    # Hozirgi vaqt: 15:13:47.328620
    # Soat: 15
    # Minut: 13
    # Sekund: 47
    # Bugungi kungi sana: 2025-01-01
    # Ertangi sana: 2025-01-02
    # Hozir vaqt: 15:13:47.328620
    # Ramazonga 59 kun qoldi!
    # 1 day, 8:31:12.671380
    # Futbol boshlanishiga 30672 s qoldi
    # Futbol boshlanishiga 511 min qoldi
    # Futbol boshlanishiga 8 soat qoldi
    # Hozir vaqt: 15:13:47
    # Sana: 01-01-25
    # 01-01-25, 15:13
