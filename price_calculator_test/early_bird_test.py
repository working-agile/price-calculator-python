import pytest
from price_calculator import TrainingCourseService, TrainingCourse

def test_should_apply_proportional_discount_from_day_6_for_csd():
    # Arrange
    """
    Days before training course: 6
    Type:                       CSD
    Full price:                 4000
    Proportional discount:      6*30
    -->
    discounted price:           4000-(6*30) = 3820
    """
    i1 = TrainingCourse("10 January 2024", 6, 50, 25, True, "CSD", 4000)
    training_courses = [i1]
    training_course_service = TrainingCourseService(training_courses)

    # Act
    training_course_service.update_current_prices()

    # Assert
    assert training_course_service.get_scheduled_training_courses()[0].current_discounted_price == 3820, "proportional discount expected"

def test_should_apply_proportional_discount_day_5_for_csd_when_enough_seats_available():
    # Arrange
    """
    Days before training course: 5
    Type:                       CSD
    Full price:                 4000
    Proportional discount:      5*30
    -->
    discounted price:           4000-(5*30) = 3850
    """
    i1 = TrainingCourse("10 January 2024", 5, 50, 25, True, "CSD", 4000)
    training_courses = [i1]
    training_course_service = TrainingCourseService(training_courses)

    # Act
    training_course_service.update_current_prices()

    # Assert
    assert training_course_service.get_scheduled_training_courses()[0].current_discounted_price == 3850, "proportional discount expected when enough seats available"

@pytest.mark.parametrize("training_course_type", ["CSPO", "CSM"])
def test_should_apply_proportional_discount_for_csm_and_cspo(training_course_type):
    # Arrange
    """
    Days before training course: 10
    Type:                       CSPO and CSM
    Full price:                 4000
    Proportional discount:      10*30
    -->
    discounted price:           4000-(10*20) = 3800
    """
    i1 = TrainingCourse("10 January 2024", 10, 50, 25, True, training_course_type, 4000)
    training_courses = [i1]
    training_course_service = TrainingCourseService(training_courses)

    # Act
    training_course_service.update_current_prices()

    # Assert
    assert training_course_service.get_scheduled_training_courses()[0].current_discounted_price == 3800, "should apply proportional discount - first day of the interval"
    