from price_calculator import ItemProcessor, Item

def test_super_early_bird_discount_overruled_by_minimum_price_for_CSD():
    # Arrange
    """
    Days before training course:    25
    type:                           CSD
    Full price (no discounts):      1200
    Minimum price CSD:              900
    -->
    SuperEarlyBird discount:        -400
    Discounted price:               800
    Minimum price:                  900
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 25, 50, 20, "CSD", 1200, 1200)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 900, "expecting the minimum price"


def test_super_early_bird_discount_overruled_by_minimum_price_for_CSM():
    # Arrange
    """
    Days before training course:    25
    type:                           CSM
    Full price (no discounts):      1200
    Minimum price CSM:              1000
    -->
    SuperEarlyBird discount:        -500
    Discounted price:               700
    Minimum price:                  1000
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 25, 50, 20, "CSM", 1200, 1200)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 1000, "expecting the minimum price"


def test_super_early_bird_discount_overruled_by_minimum_price_for_CSPO():
    # Arrange
    """
    Days before training course:    25
    type:                           CSPO
    Full price (no discounts):      1500
    Minimum price CSPO:             1200
    -->
    SuperEarlyBird discount:        -400
    Discounted price:               1100
    Minimum price:                  1200
    """
    processor = ItemProcessor()
    training_course = Item(1, "10 January 2024", 25, 50, 20, "CSPO", 1500, 1500)
    courses = [training_course]

    # Act
    updated_training_courses = processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    assert updated_training_courses[0].curr == 1200, "expecting the minimum price"
