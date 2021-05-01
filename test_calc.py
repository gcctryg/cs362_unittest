import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        #result = calc.add(10,5)
       # self.assertEqual(result, 15)
        self.assertEqual(calc.add(10, 5), 15)

class testCaseSubtra(unittest.TestCase):
    def test_add(self):
        #result = calc.add(10,5)
       # self.assertEqual(result, 15)
        self.assertEqual(calc.subtra(10, 5), 5)

class testCaseMultip(unittest.TestCase):
    def test_add(self):
        #result = calc.add(10,5)
       # self.assertEqual(result, 15)
        self.assertEqual(calc.multip(10, 5), 50)

class testCaseDiv(unittest.TestCase):
    def test_add(self):
        #result = calc.add(10,5)
       # self.assertEqual(result, 15)
        self.assertEqual(calc.div(10, 5), 2)

if __name__ == '__main__ ':
    unittest.main()