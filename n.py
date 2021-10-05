import unittest
from name import name
class Addname(unittest.TestCase):
    def testname1(self):
        self.assertEqual(name('deepu','niki'),True)
    def testname2(self):
        self.assertEqual(name('deepu','deepu'),False)
    def testname3(self):
        self.assertEqual(name('',''),False)
    def testname4(self):
        self.assertEqual(name('deepu','niki'), True)
if __name__=='__main__':
    unittest.main()

