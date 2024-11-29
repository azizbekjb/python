print("Kiritilgan sonni kvadartini chiqaruvchi dastur")
savol = "Istalgan sonni kirirting "
savol += "(to'xtatish uchun 'exit' deb yozing): "
ishora = True
while(ishora == True):
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat) ** 2)
