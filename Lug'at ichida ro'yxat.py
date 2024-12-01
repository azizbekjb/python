dasturchilar = {
    'ali' : ['python','c++'],
    'vali' : ['html','css','js'],
    'hasan' : ['php','sql'],
    'husan' : ['python','php'],
    'maryam' : ['c++','c#']
}
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()}:",end='')
    for til in tillar:
        print(f"{til.upper()} ",end='')
#NATIJA:
''' Ali:PYTHON C++ 
    Vali:HTML CSS JS 
    Hasan:PHP SQL 
    Husan:PYTHON PHP 
    Maryam:C++ C# '''
