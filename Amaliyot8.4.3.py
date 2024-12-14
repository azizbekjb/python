#Amaliyot8.4.3
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(f"Asl ro'yxat o'zgarmadi: {talabalar}")
print(baholar)
#Natija:
    # Alining bahosini kiriting: 3
    # Valining bahosini kiriting: 5
    # Hasanning bahosini kiriting: 5
    # Husanning bahosini kiriting: 4
    # Asl ro'yxat o'zgarmadi: ['ali', 'vali', 'hasan', 'husan']
    # {'ali': '3', 'vali': '5', 'hasan': '5', 'husan': '4'}
