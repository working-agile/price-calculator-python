import pytest
from price_calculator import ItemProcessor, Item
    
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
    processor = ItemProcessor()
    csd_training_course = Item(1, "10 January 2024", 6, 50, 25, "CSD", 4000, 4000)
    courses = [csd_training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 3820, "proportional discount expected"


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
    processor = ItemProcessor()
    csd_training_course = Item(1, "10 January 2024", 5, 50, 25, "CSD", 4000, 4000)
    courses = [csd_training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 3850, "proportional discount expected when enough seats available"


@pytest.mark.parametrize("training_course_type", ["CSPO", "CSM"])
def test_should_apply_proportional_discount_for_CSM_and_CSPO(training_course_type):
    # Arrange
    """
    Days before training course:    10
    Type:                           CSPO e CSM
    Full price:                     4000
    Proportional discount:          10*30
    -->
    discounted:                     4000-(10*20) = 3800
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 10, 50, 25, training_course_type, 4000, 4000)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 3800, "should apply proportional discount - first day of the interval"
