#7.2. exceptions(istisnolar)
#Ma'lum turdagi xatolarni ushlash:IndexError
numbers = [1,2,3,4]
try:
    print(numbers[5])
except IndexError:
    print(f"Ro'yxatda {len(numbers)} ta son bor xolos")
#Natija:
    #Ro'yxatda 4 ta son bor xolos
