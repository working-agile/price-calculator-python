import pytest
from price_calculator import DataProcessor
from .util_test_container_test import *

@pytest.fixture(scope="module", autouse=True)
def before_and_after_all():
    beforeAll()
    yield
    afterAll()

@pytest.fixture(scope="function", autouse=True)
def before_and_after_each():
    beforeEach()
    yield
    afterEach()

def test_prices_january_1_2025():
    # Arrange
    test_database_connection = get_database_connection()
    processor = DataProcessor(test_database_connection)
    
    # Insert test data
    cursor = test_database_connection.cursor()
    insert_queries = [
        "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(1,'9 January 2025',9,30,7,'CSPO',4000)",
        "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(2,'10 January 2025',10,30,8,'CSO',3000)",
        "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(3,'20 January 2025',20,30,27,'CSM',3000)"
    ]
    for query in insert_queries:
        cursor.execute(query)
    test_database_connection.commit()
    cursor.close()
    
    # Act - call the function
    processor.calculate_data(False)
    
    # Assert
    actual_result_course = processor.get_list()
    actual_sales_value = processor.get_sales_value()
    
    # Compare with the expected result
    assert actual_result_course[0].curr == 3820, "current price of course 1 is wrong"
    assert actual_result_course[1].curr == 2800, "current price of course 2 is wrong"
    assert actual_result_course[2].curr == 2600, "current price of course 3 is wrong"
    assert actual_sales_value == 119340, "sales target value wrong"
    
    """
    Type: CSPO
    When: 9 January 2025
    Remaining days before training course: 9
    Full Price: 4000
    Current price: 3820
    Number of seats: 30
    Remaining available seats: 7

    Type: CSO
    When: 10 January 2025
    Remaining days before training course: 10
    Full Price: 3000
    Current price: 2800
    Number of seats: 30
    Remaining available seats: 8

    Type: CSM
    When: 20 January 2025
    Remaining days before training course: 20
    Full Price: 3000
    Current price: 2600
    Number of seats: 30
    Remaining available seats: 27

    Remaining total sales target: 119340
    """

def test_prices_january_2_2025():
    # Arrange
    test_database_connection = get_database_connection()
    processor = DataProcessor(test_database_connection)
    
    # Insert test data
    cursor = test_database_connection.cursor()
    insert_queries = [
        "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(1,'9 January 2025',9,30,7,'CSPO',4000)",
        "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(2,'10 January 2025',10,30,8,'CSO',3000)",
        "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(3,'20 January 2025',20,30,27,'CSM',3000)"
    ]
    for query in insert_queries:
        cursor.execute(query)
    test_database_connection.commit()
    cursor.close()
    
    # Act - call the function
    processor.calculate_data(True)
    
    # Assert
    actual_result_course = processor.get_list()
    actual_sales_value = processor.get_sales_value()
    
    # Compare with the expected result
    assert actual_result_course[0].curr == 3840, "current price of course 1 is wrong"
    assert actual_result_course[1].curr == 2820, "current price of course 2 is wrong"
    assert actual_result_course[2].curr == 2600, "current price of course 3 is wrong"
    assert actual_sales_value == 119640, "sales target value wrong"
