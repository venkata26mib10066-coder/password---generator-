import unittest

from generator import generate_password
from validator import validate_length, validate_choice
from strength_checker import check_strength


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(12, True, True, True, True)
        self.assertEqual(len(password), 12)

    def test_valid_length(self):
        valid, message = validate_length(12)
        self.assertTrue(valid)

    def test_invalid_length(self):
        valid, message = validate_length(2)
        self.assertFalse(valid)

    def test_valid_choice(self):
        self.assertTrue(validate_choice("y"))
        self.assertTrue(validate_choice("n"))

    def test_password_strength(self):
        self.assertEqual(check_strength("Abc123!@"), "Strong")


if __name__ == "__main__":
    unittest.main()