import pytest
from price_calculator import TrainingCourseFactory

def test_the_training_course_factory_can_create_ODSF_training_courses():
    # Act
    try:
        training_course = TrainingCourseFactory.create_training_course(
            "OD-SF", "10 January 2024", 10, 20, 19, True, 3500
        )
    except ValueError:
        pytest.fail("The factory should be able to create a OD-SF training class.")

    # Assert
    assert training_course is not None
    assert training_course.get_description() == "OD-SF"

def test_odsf_training_courses_dont_have_a_scheduled_date():
    training_course = TrainingCourseFactory.create_training_course(
        "OD-SF", "10 January 2024", 10, 20, 19, True, 3500
    )
    try:
        training_course.decrease_days_before_training_course()
        pytest.fail("Not expected to come here: ODSF don't have a scheduled date")
    except RuntimeError:
        # Expected to come here!
        pass

