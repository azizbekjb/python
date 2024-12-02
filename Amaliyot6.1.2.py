#Amaliyot 6.1.2
xabar = "Yoshingizni kiriting"
_chiqish_ = "(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):"
xabar += _chiqish_
yosh = " "
while yosh != "quit" or yosh != "exit":
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
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):1
    # Siz uchun chipta narxi: 2000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):2
    # Siz uchun chipta narxi: 2000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):7
    # Siz uchun chipta narxi: 2000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):8
    # Siz uchun chipta narxi: 3000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):18
    # Siz uchun chipta narxi: 3000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):19
    # Siz uchun chipta narxi: 10000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):95
    # Siz uchun chipta narxi: tekin
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):65
    # Siz uchun chipta narxi: 10000
    # Yoshingizni kiriting(To'xtash uchun 'exit' yoki 'quit' so'zini kiriting):exit
    # 
    # Process finished with exit code 0
