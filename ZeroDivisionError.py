#7.2. exceptions(istisnolar)
#Ma'lum turdagi xatolarni ushlash:ZeroDivisionError
x,y = 5, 10
try:
    y/(x - 5)
except ZeroDivisionError:
    print("0 ga bo'linmaydi")
#Natija:
    #0 ga bo'linmaydi
