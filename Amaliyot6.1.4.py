#Amaliyot 6.1.4
xabar = "Musbat son kiriting"
_chiqish_ = "(To'xtash uchun 'exit' so'zini kiriting):"
xabar += _chiqish_
son = ' '
while True:
    son = input(xabar)
    if son == 'exit' :
        break
    elif float(son) < 0:
        continue
    else:
        ildiz = float(son)**(0.5)
        print(f"{son} ning kvadrat ildizi {ildiz} ga teng!!!")
#Natija:
    #Musbat son kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):exit
    #Process finished with exit code 0
