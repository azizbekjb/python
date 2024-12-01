hamkasblar = {
    'ali' : {
        'familiya' : 'valiyev',
        'tyil' : 1995,
        'malumot' : 'oliy',
        'tillar' : ['python','c++']
    },
    'vali' : {
            'familiya' : 'aliyev',
            'tyil' : 2001,
            'malumot' : 'oliy',
            'tillar' : ['html','css','js']
    },
    'hasan' : {
        'familiya' : 'husanov',
        'tyil' : 1999,
        'malumot' : 'oliy',
        'tillar' : ['python','php']
    }
}
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug\'ilgan. \n"
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarni biladi:")
    for til in info['tillar']:
        print(til.upper(),end=' ')
#   NATIJA:
'''Ali Valiyev, 1995-yilda tug'ilgan. 
Ma'lumoti: oliy. 
Quyidagi dasturlash tillarni biladi:
PYTHON C++ 
Vali Aliyev, 2001-yilda tug'ilgan. 
Ma'lumoti: oliy. 
Quyidagi dasturlash tillarni biladi:
HTML CSS JS 
Hasan Husanov, 1999-yilda tug'ilgan. 
Ma'lumoti: oliy. 
Quyidagi dasturlash tillarni biladi:
PYTHON PHP '''