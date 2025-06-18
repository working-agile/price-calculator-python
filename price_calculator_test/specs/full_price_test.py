import pytest
from price_calculator import ItemProcessor, Item

@pytest.mark.parametrize("training_course_type", ["CSD", "CSPO", "CSM"])
def test_should_have_full_price_on_the_day_of_the_training_class(training_course_type):
    # Arrange
    """
    Days before training course:    0
    type:                           CSD, CSPO, CSM
    Full price (no discounts):      4000
    -->
    no discount:                    4000
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 0, 50, 20, training_course_type, 4000, 4000)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 4000, "expecting the full price"


@pytest.mark.parametrize("training_course_type", ["CSD", "CSPO", "CSM"])
def test_should_have_full_price_on_the_day_prior_to_the_training_class(training_course_type):
    # Arrange
    """
    Days before training course:    1
    Full price (no discounts):      4000
    -->
    no discount:                    4000
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 1, 50, 20, training_course_type, 4000, 4000)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 4000, "expecting the full price"


@pytest.mark.parametrize("training_course_type", ["CSD", "CSPO", "CSM"])
def test_full_price_5_days_prior_to_the_training_class_if_less_than_3_seats_left(training_course_type):
    # Arrange
    """
    Days before training course:    5
    Seats left:                     2
    Full price (no discounts):      4000
    -->
    no discount:                    4000
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 5, 50, 2, training_course_type, 4000, 4000)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 4000, "expecting the full price"
