import pytest
from .calculator import Calculator

def test_should_add_amount_to_value():
    # Arrange
    calculator = Calculator(0)

    # Act
    calculator.add(100)

    # Assert
    actual_value = calculator.get_value()
    assert actual_value == 100
