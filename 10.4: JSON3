#10.4: JSON
#JSON - JavaScript Object Notation
#json.dump() - ma'lumotlarni json formatiga o'tkazish va  faylga yozish
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
with open('bemor.json', 'w') as file:
    json.dump(bemor, file)
bemor_json = json.dumps(bemor)
#Natija:
    # Process finished with exit code 0
