#12.1: pprint - chiroyli print
import json
from pprint import pprint
filename = 'bemor.json'
with open(filename) as file:
    bemor = json.load(file)
#oddiy print
print(f"Oddiy print: {bemor}")

#Chiroyli print
print("Chiroyli print")
pprint(bemor)
#Natija:
    # Oddiy print: {'ism': 'Alijon Valiyev', 'yosh': 20, 'oila': True, 'farzandlar': ['Ahmad', 'Bonu'], 'allergiya': None, 'dorilar': [{'nomi': 'Analgin', 'miqdori': 0.5}, {'nomi': 'Panadol', 'miqdori': 1.2}]}
    # Chiroyli print
    # {'allergiya': None,
    #  'dorilar': [{'miqdori': 0.5, 'nomi': 'Analgin'},
    #              {'miqdori': 1.2, 'nomi': 'Panadol'}],
    #  'farzandlar': ['Ahmad', 'Bonu'],
    #  'ism': 'Alijon Valiyev',
    #  'oila': True,
    #  'yosh': 20}
