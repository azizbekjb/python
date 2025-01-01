#Amaliyot12.1
#4
import re
andoza = r"^\+998.........$"
tel_raqam = input("O'zbekiston hududiga mos telefon raqam kiriting('+' belgisi bilan kiriting): ")
if re.match(andoza, tel_raqam):
    print("Raqam qabul qilindi")
else:
    print("Raqam qabul qilinmadi")
#Natija:
    # O'zbekiston hududiga mos telefon raqam kiriting('+' belgisi bilan kiriting): +998931234567
    # Raqam qabul qilindi
