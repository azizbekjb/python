#11.1: Sonlarni tekshirish
import unittest
from circle import getArea, getPerimeter
class CircleTest(unittest.TestCase):
    #Test metodlar har doim 'test' so'zidan boshlanishi kerak
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3), 28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
unittest.main()
    # ..
    # ----------------------------------------------------------------------
    # Ran 2 tests in 0.000s
    # OK
