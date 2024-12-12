#Amaliyot8.3.4
from math import*
def aylana(R):
    yechimlar = {
        'radius' : R,
        'diametr' : 2*R,
        'uzunlik' : 2*R*pi,
        'yuza' : pi*R**2
    }
    return yechimlar
R = float(input("Radiusni kirit: "))
malumotlar = aylana(R)
print(f"Malumotlar:\n"
      f"Radiusi: {malumotlar['radius']:.2f}\n"
      f"Diametri: {malumotlar['diametr']:.2f}\n"
      f"Uzunligi: {malumotlar['uzunlik']:.2f}\n"
      f"Yuza: {malumotlar['yuza']:.2f}")
#Natija:
    # Radiusni kirit: 4.23
    # Malumotlar:
    # Radiusi: 4.23
    # Diametri: 8.46
    # Uzunligi: 26.58
    # Yuza: 56.21
