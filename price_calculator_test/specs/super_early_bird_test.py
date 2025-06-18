from price_calculator import ItemProcessor, Item

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
    training_course = Item(1, "21 January 2024", 11, 50, 20, "CSD", 4000, 4000)
    courses = [training_course]
    processor = ItemProcessor()

    # Act
    updated_training_courses = processor.process_items(courses, False)

    # Assert
    assert updated_training_courses[0].curr == 3600

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
    training_course = Item(1, "10 January 2024", 25, 50, 20, "CSD", 4000, 4000)
    courses = [training_course]
    processor = ItemProcessor()

    # Act
    updated_training_courses = processor.process_items(courses, False)

    # Assert
    assert updated_training_courses[0].curr == 3600

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
    training_course = Item(1, "10 January 2024", 25, 50, 20, "CSM", 4000, 4000)
    courses = [training_course]
    processor = ItemProcessor()

    # Act
    updated_training_courses = processor.process_items(courses, False)

    # Assert
    assert updated_training_courses[0].curr == 3500

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
    training_course = Item(1, "10 January 2024", 32, 50, 20, "CSPO", 4000, 4000)
    courses = [training_course]
    processor = ItemProcessor()

    # Act
    updated_training_courses = processor.process_items(courses, False)

    # Assert
    assert updated_training_courses[0].curr == 3600
