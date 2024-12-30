#Amaliyot10.4.2
#2, 3
import json
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(talaba)
with open('ism.json', 'w') as file:
    json.dump(talaba['ism'], file)
with open('familiya.json', 'w') as file:
    json.dump(talaba['familiya'], file)
