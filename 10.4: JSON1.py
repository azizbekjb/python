#10.4: JSON
#JSON - JavaScript Object Notation
#json.dumps()
import json
x = 10
x_json = json.dumps(x)
ism = 'Azizbek'
ism_json = json.dumps(ism)
sonlar = [1, 3, 5, 7]
sonlar_json = json.dumps(sonlar)
print(ism_json)
print(x_json)
print(sonlar_json)
#Natija:
    # "Azizbek"
    # 10
    # [1, 3, 5, 7]
