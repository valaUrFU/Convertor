import unittest
from Convertor import convert_from_decimal, convert_to_decimal


class ConvertTest(unittest.TestCase):
    def test_dec_to_base_2(self):
        self.assertEqual(convert_from_decimal(10, 2), '1010')

    def test_dec_to_base_16(self):
        self.assertEqual(convert_from_decimal(255, 16), 'FF')

    def test_dec_to_base_8(self):
        self.assertEqual(convert_from_decimal(63, 8), '77')

    def test_dec_to_base_36(self):
        self.assertEqual(convert_from_decimal(1234567890, 36), 'KF12OI')

    def test_zero(self):
        self.assertEqual(convert_from_decimal(0, 2), '0')

    def test_negative(self):
        self.assertEqual(convert_from_decimal(-10, 2), '-1010')

    def test_large_number(self):
        self.assertEqual(convert_from_decimal(10 ** 18, 36), '7LIEEXZX4KXS')

    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            convert_from_decimal(10, 37)

    def test_base_2_to_dec(self):
        self.assertEqual(convert_to_decimal('1010', 2), 10)

    def test_base_16_to_dec(self):
        self.assertEqual(convert_to_decimal('FF', 16), 255)

    def test_base_8_to_dec(self):
        self.assertEqual(convert_to_decimal('77', 8), 63)

    def test_base_36_to_dec(self):
        self.assertEqual(convert_to_decimal('KF12OI', 36), 1234567890)

    def test_zero_to_dec(self):
        self.assertEqual(convert_to_decimal('0', 2), 0)

    def test_negative_to_dec(self):
        self.assertEqual(convert_to_decimal('-1010', 2), -10)

    def test_large_number_to_dec(self):
        self.assertEqual(convert_to_decimal('7LIEEXZX4KXS', 36), 10**18)

    def test_invalid_digit_to_dec(self):
        with self.assertRaises(ValueError):
            convert_to_decimal('G', 16)

    def test_invalid_base_to_dec(self):
        with self.assertRaises(ValueError):
            convert_to_decimal('10', 37)
