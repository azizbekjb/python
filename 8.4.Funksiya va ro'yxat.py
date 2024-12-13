#8.4.Funksiya va ro'yxat
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
#Natija:
    # Husanning bahosini kiriting: 5
    # Hasanning bahosini kiriting: 4
    # Valining bahosini kiriting: 4
    # Alining bahosini kiriting: 3
    # {'husan': '5', 'hasan': '4', 'vali': '4', 'ali': '3'}
