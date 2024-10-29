from price_calculator import DataProcessor, TrainingCourse

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
    i1 = TrainingCourse("10 January 2024", 30, 50, 5, True, "CSD", 4000)
    
    """
    Number of seats:                2
    Days before training course:    9
    Type:                           CSD
    Full price:                     4000
    Super Early bird discount:      9*30
    Discounted price:               3500
    """
    i2 = TrainingCourse("10 January 2024", 9, 50, 2, True, "CSD", 4000)
    
    training_courses = [i1, i2]
    processor = DataProcessor(training_courses)

    # Act
    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(False)

    # Assert
    expected_remaining_sales_target = (3600 * 5) + ((4000 - 9*30) * 2)
    assert processor.get_remaining_sales_target() == expected_remaining_sales_target
