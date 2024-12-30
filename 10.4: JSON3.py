#10.4: JSON
#JSON - JavaScript Object Notation
#json.load() va json.loads()
#json.loads() - ma'lumotlarni jsondan pythonga o'tkazish
#json.load() - fayldan ma'lumotlarni o'qib uni pythonga o'tkazish
import json
bemor = {
    'ism' : 'Alijon Valiyev',
    'yosh' : 20,
    'oila' : True,
    "farzandlar" : ("Ahmad", "Bonu"),
    'allergiya' : None,
    "dorilar" : [
        {'nomi' : 'Analgin', 'miqdori' : 0.5},
        {'nomi' : 'Panadol', 'miqdori' : 1.2}
    ]
}
bemor_json = json.dumps(bemor)
bemor = json.loads(bemor_json)
print(bemor)

#Jsondan pythonga
with open('bemor.json') as file:
    json.load(file)
print(type(bemor))
#Natija:
    # {'ism': 'Alijon Valiyev', 'yosh': 20, 'oila': True, 'farzandlar': ['Ahmad', 'Bonu'], 'allergiya': None, 'dorilar': [{'nomi': 'Analgin', 'miqdori': 0.5}, {'nomi': 'Panadol', 'miqdori': 1.2}]}
    # <class 'dict'>
