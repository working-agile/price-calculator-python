from price_calculator import ItemProcessor, Item

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
    csd1 = Item(1, "20 February 2024", 41, 50, 5, "CSD", 4000, 4000)
    """
    Number of seats:                2
    Days before training course:    9
    Type:                           CSD
    Full price:                     4000
    Super Early bird discount:      9*30
    Discounted price:               3500
    """
    csd2 = Item(2, "19 January 2024", 9, 50, 2, "CSD", 4000, 4000)
    courses = [csd1, csd2]
    processor = ItemProcessor()

    # Act
    processor.process_items(courses, False)  # just recalculate the current discounted price

    # Assert
    expected_remaining_sales_target = (3600 * 5) + ((4000 - 9 * 30) * 2)
    assert processor.get_sales_value() == expected_remaining_sales_target