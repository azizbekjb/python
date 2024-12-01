#   1-masala
mashhur_1= {
    'Ismi' : 'Alisher Navoiy',
    'tyil' : 1441,
    'tjoy' : 'Qadimgi Xuroson davlati,Hirot shahri',
    'kasbi' : 'shoir',
    'asarlari' : ['Xamsa', 'Mahbubul-qulub']
}
mashhur_2= {
    'Ismi' : 'Abu Ali ibn Sino',
    'tyil' : 918,
    'tjoy' : 'Qadimgi Movarounnahr davlati,Buxoro shahri',
    'kasbi' : 'tabib',
    'asarlari' : ['Tib qonunlari', 'Kitob as-shifo']
}
mashhur_3= {
    'Ismi' : 'Muso Al-Xorazmiy',
    'tyil' : 783,
    'tjoy' : 'Qadimgi Movarounnahr davlati,Xorazm shahri',
    'kasbi' : 'matematik,astranom',
    'asarlari' : ['Al-jabr val-muqobala','Arifmetika']
}
mashhur_4= {
    'Ismi' : 'Abu Rayhon Beruniy',
    'tyil' : 973,
    'tjoy' : 'Qadimgi Movarounnahr davlati,Xorazm shahri',
    'kasbi' : 'fizik olim',
    'asarlari' : ['Kitob at-Tafhim','Risola al-Beruniy']
}
mashhurlar = [mashhur_1,mashhur_2,mashhur_3,mashhur_4]
for mashhur in mashhurlar:
    print(f"{mashhur['Ismi']} {mashhur['tyil']}-yilda {mashhur['tjoy']}da tug'ilgan.U juda mashhur\n{mashhur['kasbi']}")

#   2-masala
for mashhur in mashhurlar:
    print(f"{mashhur['Ismi']} asarlari:")
    for asar in mashhur['asarlari']:
        print(asar)