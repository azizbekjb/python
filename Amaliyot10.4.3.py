#Amaliyot10.4.3
#4
import json
filename = 'C:\\Users\\User\\Downloads\\students.json'
with open(filename) as file:
    students = json.load(file)
print(students)
students1 = students["student"]

# Har bir talabani konsolga chiqaramiz
for student in students1:
    print(f"{student['name']} {student['lastname']}, {student['year']} - kurs, {student['faculty']} talabasi")
    
#Natija:
    # {'student': [{'id': '01', 'name': 'Tom', 'lastname': 'Price', 'year': 4, 'faculty': 'Engineering'},
    #              {'id': '02', 'name': 'Nick', 'lastname': 'Thameson', 'year': 3, 'faculty': 'Computer Science'},
    #              {'id': '03', 'name': 'John', 'lastname': 'Doe', 'year': 2, 'faculty': 'ICT'}]}
    # Tom
    # Price, 4 - kurs, Engineering
    # talabasi
    # Nick
    # Thameson, 3 - kurs, Computer
    # Science
    # talabasi
    # John
    # Doe, 2 - kurs, ICT
    # talabasi
