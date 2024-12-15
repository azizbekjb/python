import random as r #Random modulini r kabi chaqiramiz
#Ixtiyoriy son tanlash
son = r.randint(0, 100)
print(f"Random: {son}")

#Ro'yxatdan ixtiyoriy son tanlash
x = list(range(0, 51, 5))
print(x)
son = r.choice(x)
print(f"Choise: {son}")

#Ro'yxatni aralashtib tashlash
y = list(range(11))
print(y)
r.shuffle(y)
print(f"Shuffle: {y}")

#Ro'yxatdan n ta elementni tanlab olish
z = list(range(100))
b = r.sample(z, k=9)
print(f"Sample: {b}")
#Natiaj:
    #Random: 52
    # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    # Choise: 25
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Shuffle: [7, 10, 6, 9, 0, 3, 8, 2, 4, 1, 5]
    # Sample: [55, 74, 30, 99, 28, 33, 11, 83, 4]
