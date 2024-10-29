import pytest
from price_calculator import TrainingCourseService, TrainingCourse

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
    i1 = TrainingCourse("10 January 2024", 0, 50, 20, True, training_course_type, 4000)
    training_courses = [i1]
    training_course_service = TrainingCourseService(training_courses)

    # Act
    training_course_service.update_current_prices()

    # Assert
    assert training_course_service.get_scheduled_training_courses()[0].current_discounted_price == 4000

@pytest.mark.parametrize("training_course_type", ["CSD", "CSPO", "CSM"])
def test_should_have_full_price_on_the_day_prior_to_the_training_class(training_course_type):
    # Arrange
    """
    Days before training course:    1
    Full price (no discounts):      4000
    -->
    no discount:                    4000
    """
    i1 = TrainingCourse("10 January 2024", 1, 50, 20, True, training_course_type, 4000)
    training_courses = [i1]
    training_course_service = TrainingCourseService(training_courses)

    # Act
    training_course_service.update_current_prices()

    # Assert
    assert training_course_service.get_scheduled_training_courses()[0].current_discounted_price == 4000

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
    i1 = TrainingCourse("10 January 2024", 5, 50, 2, True, training_course_type, 4000)
    training_courses = [i1]
    training_course_service = TrainingCourseService(training_courses)

    # Act
    training_course_service.update_current_prices()

    # Assert
    assert training_course_service.get_scheduled_training_courses()[0].current_discounted_price == 4000
    