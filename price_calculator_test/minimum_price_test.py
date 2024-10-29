from price_calculator import DataProcessor, Item

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
    i1 = Item("10 January 2024", 25, 50, 20, True, "CSD", 1200)
    items = [i1]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    assert DataProcessor.list[0].current == 900

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
    i1 = Item("10 January 2024", 25, 50, 20, True, "CSM", 1500)
    items = [i1]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    assert DataProcessor.list[0].current == 1000

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
    i1 = Item("10 January 2024", 25, 50, 20, True, "CSPO", 1500)
    items = [i1]
    DataProcessor.list = items

    # Act
    DataProcessor.calculate_data(False)

    # Assert
    assert DataProcessor.list[0].current == 1200
