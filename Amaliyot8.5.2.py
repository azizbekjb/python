#Amaliyot8.5.2
def malumot(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
talaba1 = malumot('Azizbek', 'Jabborov', yoshi = 18, manzili = 'Samarkand')
print(talaba1)
#Natija:
    #{'yoshi': 18, 'manzili': 'Samarkand', 'ism': 'Azizbek', 'familiya': 'Jabborov'}
