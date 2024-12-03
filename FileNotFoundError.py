#7.2. exceptions(istisnolar)
#Ma'lum turdagi xatolarni ushlash:FileNotFoundError
file = 'data.txt'   #bunday fayl mavjud emas
try:
    f = open(file)
except FileNotFoundError:
    print(f"{file} fayli mavjud emas")
#Natija:
    #data.txt fayli mavjud emas
