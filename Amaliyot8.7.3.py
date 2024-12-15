#Amaliyot8.7.3
import random as r
sonlar = r.sample(range(1000), 10)
print(f"10ta son :{sonlar}")
print(f"10ta sonning kvadrati: {list(map(lambda x : x**2, sonlar))}")
print(f"10ta sonlar orasida toqlari: {list(filter(lambda x : x % 2 == 1, sonlar))}")
#Natija:
    # 10ta son :[723, 456, 548, 142, 404, 289, 848, 181, 705, 965]
    # 10ta sonning kvadrati: [522729, 207936, 300304, 20164, 163216, 83521, 719104, 32761, 497025, 931225]
    # 10ta sonlar orasida toqlari: [723, 289, 181, 705, 965]
