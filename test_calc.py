import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        #result = calc.add(10,5)
       # self.assertEqual(result, 15)
        self.assertEqual(calc.add(10, 5), 14)

    def test_type(self):
        self.assertRaises(TypeError)

class testCaseSubtra(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.subtra(10, 5), 5)

    def test_type(self):
        self.assertRaises(TypeError)

class testCaseMultip(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.multip(10, 5), 50)

    def test_type(self):
        self.assertRaises(TypeError)

class testCaseDiv(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.div(10, 5), 2)

    def test_type(self):
        self.assertRaises(TypeError)
        
if __name__ == '__main__ ':
    unittest.main()