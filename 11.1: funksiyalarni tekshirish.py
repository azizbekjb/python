#11.1: funksiyalarni tekshirish
import unittest
from name import get_full_name
class NameTest(unittest.TestCase):
    #Test metodlar har doim 'test' so'zidan boshlanishi kerak
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon', 'valiyev')
        self.assertEqual(formatted_name, 'Alijon Valiyev')
    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan', 'husanov', 'olimovich')
        self.assertEqual(name, 'Hasan Olimovich Husanov')
unittest.main()
    # ..
    # ----------------------------------------------------------------------
    # Ran 2 tests in 0.000s
    # OK
