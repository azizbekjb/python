#Klaslarni import qilish

#Bitta klassni import qilish
from odamlar import Talaba
from transport import Avto

#Bir nechta klasslarni import qilish
from odamlar import Talaba, Shaxs, Professor

#Modul ichidagi barcha klasslarni import qilish
from odamlar import *
talaba = Talaba('Azizbek', 'Jabborov', "AA1111110", 2006, "A1110101")
avto = Avto("GM", "Gentra", "Oq", 2019, 9100)
