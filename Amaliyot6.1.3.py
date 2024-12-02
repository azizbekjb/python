#Amaliyot 6.1.3
xabar = "Yoshingizni kiriting"
_chiqish_ = "(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):"
xabar += _chiqish_
yosh = " "
while True:
    yosh = input(xabar)
    if yosh == "quit" or yosh == "exit":
        break
    print("Siz uchun chipta narxi: ",end="")
    if int(yosh) <= 7:
        print(2000)
    elif 7 < int(yosh) <= 18:
        print(3000)
    if 18 < int(yosh) <= 65:
        print(10000)
    elif int(yosh) > 65:
        print("tekin")

#Natija:
    #Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):exit
    #Process finished with exit code 0
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):quit
    # Process finished with exit code 0
