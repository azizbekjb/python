#7.2. exceptions(istisnolar)
#Xatolarni ko'rsatmay o'tish:pass
user = {
    'name' : 'Azizbek',
    'age' : '18'
}
key = 'tel'
try:
    print(f"Foydalanuvxhi: {user[key]}")
except KeyError:
    pass
#Natija:
    #
