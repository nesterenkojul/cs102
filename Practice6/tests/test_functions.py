import unittest
import functions


class FunctionsTestCase(unittest.TestCase):
    def test_is_real(self):
        self.assertFalse(functions.is_real("0.000"))
        self.assertTrue(functions.is_real("0.0011"))
        self.assertFalse(functions.is_real("34.000"))
        self.assertTrue(functions.is_real("222.0201"))
        self.assertFalse(functions.is_real("0.w32e32"))
        self.assertTrue(functions.is_real("0"))
        self.assertFalse(functions.is_real("abc"))
        self.assertFalse(functions.is_real(".534"))
        self.assertFalse(functions.is_real("67.54.34"))
    
    def test_check_password(self):
        self.assertFalse(functions.check_password("044516341440"))
        self.assertTrue(functions.check_password("fiTUR865//78!87a"))
        self.assertFalse(functions.check_password("utTR9%1"))
        self.assertFalse(functions.check_password("asdfgh345df546fgh"))
        self.assertFalse(functions.check_password("ASDFassssadftWER"))
        self.assertFalse(functions.check_password("er1hDFhHG7JH78hj9"))


if __name__ == '__main__':
    unittest.main()