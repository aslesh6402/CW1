import unittest
import phonenumbers
from main import parse_phone_number  # Adjust with your actual function

class TestPhoneNumberParsing(unittest.TestCase):
    def test_valid_number(self):
        number = "+9779866296130"
        result = parse_phone_number(number)
        self.assertTrue(phonenumbers.is_valid_number(result))

    def test_invalid_number(self):
        number = "123"
        with self.assertRaises(ValueError):
            parse_phone_number(number)

if __name__ == '__main__':
    unittest.main()
