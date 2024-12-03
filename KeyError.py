#7.2. exceptions(istisnolar)
#Ma'lum turdagi xatolarni ushlash:KeyError
user = {
    'name' : 'Azizbek',
    'age' : '18'
}
key = 'tel'
try:
    print(f"Foydalanuvxhi: {user[key]}")
except KeyError:
    print(f"Bunday kalit mavjud emas")
#Natija:
    #Bunday kalit mavjud emas
