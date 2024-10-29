from price_calculator import DataProcessor, TrainingCourse

def test_super_early_bird_discount_on_day_11_before_training_course():
    # Arrange
    """
    Days before training course:    11
    type:                           CSD
    Full price (no discounts):      4000
    SuperEarlyBird discount:        -400
    -->
    discounted price:               3600
    """
    i1 = TrainingCourse("10 January 2024", 11, 50, 20, True, "CSD", 4000)
    training_courses = [i1]
    processor = DataProcessor(training_courses)

    # Act
    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(False)

    # Assert
    assert processor.get_scheduled_training_courses()[0].current_discounted_price == 3600

def test_super_early_bird_discount_for_CSD():
    # Arrange
    """
    Days before training course:    25
    type:                           CSD
    Full price (no discounts):      4000
    -->
    SuperEarlyBird discount:        -400
    Discounted price:               3600
    """
    i1 = TrainingCourse("10 January 2024", 25, 50, 20, True, "CSD", 4000)
    training_courses = [i1]
    processor = DataProcessor(training_courses)

    # Act
    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(False)

    # Assert
    assert processor.get_scheduled_training_courses()[0].current_discounted_price == 3600

def test_super_early_bird_discount_for_CSM():
    # Arrange
    """
    Days before training course:    25
    type:                           CSM
    Full price (no discounts):      4000
    -->
    SuperEarlyBird discount:        -500
    Discounted price:               3500
    """
    i1 = TrainingCourse("10 January 2024", 25, 50, 20, True, "CSM", 4000)
    training_courses = [i1]
    processor = DataProcessor(training_courses)

    # Act
    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(False)

    # Assert
    assert processor.get_scheduled_training_courses()[0].current_discounted_price == 3500

def test_super_early_bird_discount_for_CSPO():
    # Arrange
    """
    Days before training course:    32
    type:                           CSPO
    Full price (no discounts):      4000
    -->
    SuperEarlyBird discount:        -400
    Discounted price:               3600
    """
    i1 = TrainingCourse("10 January 2024", 32, 50, 20, True, "CSPO", 4000)
    training_courses = [i1]
    processor = DataProcessor(training_courses)

    # Act
    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(False)

    # Assert
    assert processor.get_scheduled_training_courses()[0].current_discounted_price == 3600
