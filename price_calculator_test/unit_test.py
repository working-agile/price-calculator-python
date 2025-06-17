import pytest
from price_calculator import DataProcessor

@pytest.mark.skip
def test_some_unit_test():
    # Arrange
    processor = DataProcessor()
    # TODO insert data

    # Act - call the function
    processor.calculate_data(False)

    # Assert
    actual_result = DataProcessor.list
    # TODO compare with the expected result
    