def salom_ber(ism):
    """Foydalanuvchiga salom beruvchi funksiya""" #<-DOCSTRING
    print(f"Assalomu alaykum {ism.title()}!")
salom_ber('Azizbek')
#parametr nomi bilan uzatish
salom_ber(ism = 'azizbek')
print(salom_ber.__doc__)
