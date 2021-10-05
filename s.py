import unittest
from validate import validate


class Validtest(unittest.TestCase):
    def testval1(self):
        self.assertEqual(validate('Nikhitha', 'niki200'), False)

    def testval2(self):
        self.assertEqual(validate('Niki', 'Niki$200'), False)

    def testval3(self):
        self.assertEqual(validate('niki', 'niki@2003'), False)

    def testval4(self):
        self.assertEqual(validate(1234, 'niki#200'), False)

    def testval5(self):
            self.assertEqual(validate('nikith', 'niki@200'),False)

    def setUP(self):
            print("setup")

    def teardown(self):
            print("teardown")

if __name__=='__main__':
    unitetst.main()