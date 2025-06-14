import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Test cases for the add method
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(0, self.calc.add(0, 0))
    
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())



    #Test cases for the substract method
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(1, self.calc.substract(2, 1))
        self.assertEqual(-1, self.calc.substract(1, 2))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertEqual(2, self.calc.substract(5, 3))
        self.assertEqual(-3, self.calc.substract(2, 5))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

        
    # Test cases for the multiply method
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(6, self.calc.multiply(3, 2))
        self.assertEqual(-6, self.calc.multiply(-3, 2))
        self.assertEqual(6, self.calc.multiply(-3, -2))
        self.assertEqual(0, self.calc.multiply(0, 0))


    # Test cases for the divide method    
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(0, self.calc.divide(0, 2))
        self.assertEqual(-1, self.calc.divide(-2, 2))
        self.assertEqual(1, self.calc.divide(-2, -2))
        self.assertEqual(0.5, self.calc.divide(1, 2))
        self.assertEqual(-0.5, self.calc.divide(-1, 2))
        self.assertEqual(-0.5, self.calc.divide(1, -2))

    # Test cases for the power method
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(0, self.calc.power(0, 2))
        self.assertEqual(1, self.calc.power(0, 0))
    
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    # Test cases for the sqrt method
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(1, self.calc.sqrt(1))
        self.assertEqual(3, self.calc.sqrt(9))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "4")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())
    
    def test_sqrt_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.sqrt, -4)
        self.assertRaises(TypeError, self.calc.sqrt, -1)
        self.assertRaises(TypeError, self.calc.sqrt, -0.1)

    # Test cases for the log10 method
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(-1, self.calc.log10(0.1))
    
    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "4")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_log10_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.log10, -4)
        self.assertRaises(TypeError, self.calc.log10, -1)
        self.assertRaises(TypeError, self.calc.log10, -0.1)

    def test_log10_method_fails_with_zero(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -0)
        self.assertRaises(TypeError, self.calc.log10, -0.0)
    
    # Test cases for the check_types method
    def test_check_types_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_types, "2", 2)
        self.assertRaises(TypeError, self.calc.check_types, 2, "2")
        self.assertRaises(TypeError, self.calc.check_types, "2", "2")
        self.assertRaises(TypeError, self.calc.check_types, None, 2)
        self.assertRaises(TypeError, self.calc.check_types, 2, None)
        self.assertRaises(TypeError, self.calc.check_types, object(), 2)
        self.assertRaises(TypeError, self.calc.check_types, 2, object())
        
    def test_check_types_method_passes_with_valid_parameters(self):
        self.assertEqual(None, self.calc.check_types(2, 2))
        self.assertEqual(None, self.calc.check_types(2.0, 2.0))
        self.assertEqual(None, self.calc.check_types(2, 2.0))
        self.assertEqual(None, self.calc.check_types(2.0, 2))
        self.assertEqual(None, self.calc.check_types(-2, -2))
        self.assertEqual(None, self.calc.check_types(-2.0, -2.0))
        self.assertEqual(None, self.calc.check_types(-2, -2.0))
        self.assertEqual(None, self.calc.check_types(-2.0, -2))
        self.assertEqual(None, self.calc.check_types(0, 0))
        self.assertEqual(None, self.calc.check_types(0.0, 0.0))

    #Test cases for the check_single_type method
    def test_check_single_type_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_single_type, "2")
        self.assertRaises(TypeError, self.calc.check_single_type, None)
        self.assertRaises(TypeError, self.calc.check_single_type, object())
        
    def test_check_single_type_method_passes_with_valid_parameters(self):
        self.assertEqual(None, self.calc.check_single_type(2))
        self.assertEqual(None, self.calc.check_single_type(2.0))
        self.assertEqual(None, self.calc.check_single_type(-2))
        self.assertEqual(None, self.calc.check_single_type(-2.0))
        self.assertEqual(None, self.calc.check_single_type(0))
        self.assertEqual(None, self.calc.check_single_type(0.0))

    def test_multiply_method_raises_invalid_permissions(self):
        with patch("app.util.validate_permissions", retEntornos_CI_CDurn_value=False):
            with self.assertRaises(InvalidPermissions) as context:
                self.calc.multiply(2, 3)
            self.assertEqual(str(context.exception), "User has no permissions")

if __name__ == "__main__":  
    unittest.main()
