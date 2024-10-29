import pytest
from price_calculator import DataProcessor, Item

def test_should_calculate_total_value_of_remaining_training_courses():
    # Arrange
    """
    Number of seats:                5
    Days before training course:    30
    Type:                           CSD
    Full price:                     4000
    super early bird discount:      400
    Discounted price:               3600
    """
    i1 = Item("10 January 2024", 30, 50, 5, True, "CSD", 4000)
    
    """
    Number of seats:                2
    Days before training course:    9
    Type:                           CSD
    Full price:                     4000
    Super Early bird discount:      9*30
    Discounted price:               3500
    """
    i2 = Item("10 January 2024", 9, 50, 2, True, "CSD", 4000)
    
    items = [i1, i2]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    expected_remaining_sales_target = (3600 * 5) + ((4000 - 9*30) * 2)
    assert DataProcessor.value == expected_remaining_sales_target
    