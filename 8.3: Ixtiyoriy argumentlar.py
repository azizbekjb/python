#8.3: Ixtiyoriy argumentlar
def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:# matn bo'sh bo'lmasa
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism
odam1 = toliq_ism_yasa('Azizbek', 'Jabborov')
odam2 = toliq_ism_yasa('Azizbek', 'Jabborov', 'Alisherovich')
print("1-Natija:", odam1,'\n'
      "2-Natija:",odam2)
#Natijalar:
    # 1-Natija: Azizbek Jabborov 
    # 2-Natija: Azizbek Alisherovich Jabborov
