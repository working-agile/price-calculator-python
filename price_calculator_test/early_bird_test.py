import pytest
from price_calculator import DataProcessor, Item
    
def test_should_apply_proportional_discount_from_day_6_for_CSD():
    # Arrange
    """
    Days before training course:    6
    Type:                           CSD
    Full price:                     4000
    Proportional discount:          6*30
    -->
    discounted price:               4000-(6*30) = 3820
    """
    i1 = Item("10 January 2024", 6, 50, 25, True, "CSD", 4000)
    items = [i1]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    assert DataProcessor.list[0].current == 3820, "proportional discount expected"

def test_should_apply_proportional_discount_day_5_for_CSD_when_enough_seats_available():
    # Arrange
    """
    Days before training course:    5
    Type:                           CSD
    Full price:                     4000
    Proportional discount:          5*30
    -->
    discounted:                     4000-(5*30) = 3850
    """
    i1 = Item("10 January 2024", 5, 50, 25, True, "CSD", 4000)
    items = [i1]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    assert DataProcessor.list[0].current == 3850, "proportional discount expected when enough seats available"

@pytest.mark.parametrize("trainingCourseType", ["CSPO", "CSM"])
def test_should_apply_proportional_discount_for_CSM_and_CSPO(trainingCourseType):
    # Arrange
    """
    Days before training course:    10
    Type:                           CSPO e CSM
    Full price:                     4000
    Proportional discount:          10*30
    -->
    discounted:                     4000-(10*20) = 3800
    """
    i1 = Item("10 January 2024", 10, 50, 25, True, trainingCourseType, 4000)
    items = [i1]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    assert DataProcessor.list[0].current == 3800, "should apply proportional discount - first day of the interval"
    