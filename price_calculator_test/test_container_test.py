import psycopg2
from testcontainers.postgres import PostgresContainer
import pytest
from price_calculator import DataProcessor

@pytest.fixture(scope="module", autouse=True)
def db_connection():
    postgres = PostgresContainer("postgres:16-alpine")
    postgres.start()
    conn = psycopg2.connect(
        dbname=postgres.dbname,
        user=postgres.username,
        password=postgres.password,
        host=postgres.get_container_host_ip(),
        port=postgres.get_exposed_port(5432)
    )

    yield conn

    conn.close()
    postgres.stop()

@pytest.fixture(scope="function", autouse=True)
def setup_database(db_connection):
    create_customers_table_if_not_exists(db_connection)
    create_test_training_courses(db_connection)

def create_customers_table_if_not_exists(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tr_crs (
                id BIGINT NOT NULL,
                tr_date VARCHAR(20) NOT NULL,
                days INTEGER,
                ttl_seats INTEGER,
                avail INTEGER,
                type CHAR(10),
                curr_price INTEGER,
                full_price INTEGER
            )
            """
        )
        conn.commit()
        cursor.close()
    except Exception as e:
        raise RuntimeError(e)

def create_test_training_courses(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tr_crs(id, tr_date, days, ttl_seats, avail, type, full_price)
            VALUES (1, '9 January 2025', 9, 30, 7, 'CSPO', 4000);
            INSERT INTO tr_crs(id, tr_date, days, ttl_seats, avail, type, full_price)
            VALUES (2, '10 January 2025', 10, 30, 8, 'CSD', 3000);
            INSERT INTO tr_crs(id, tr_date, days, ttl_seats, avail, type, full_price)
            VALUES (3, '20 January 2025', 20, 30, 27, 'CSM', 3000);
            """
        )
        conn.commit()
        cursor.close()
        print("------------ created ------------------")
    except Exception as e:
        raise RuntimeError(e)

def test_manual_tests_simulating_test_database(db_connection):
    DataProcessor.set_test_connection(db_connection)

    # 1. Show the current prices
    processor = DataProcessor.get_instance()
    processor.calculate_data(False)

    print("Scheduled training courses:")
    for item in processor.list:
        print("------------------------------")
        print(f"Type: {item.type}")
        print(f"When: {item.tr_date}")
        print(f"Remaining days before training course: {item.days}")
        print(f"Full Price: {item.full}")
        print(f"Current price: {item.curr}")
        print(f"Number of seats: {item.seats}")
        print(f"Remaining available seats: {item.avail}")

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {processor.sales_value}")
    print("-----------------------------------------------------")

    # 2. Move to next day
    print("\n\nMove to next day\n")
    processor.calculate_data(True)

    for item in processor.list:
        print("Current training courses:")
        print("------------------------------")
        print("Training course")
        print(f"Type: {item.type}")
        print(f"When: {item.tr_date}")
        print(f"Remaining days before training course: {item.days}")
        print(f"Full Price: {item.full}")
        print(f"Current price: {item.curr}")
        print(f"Number of seats: {item.seats}")
        print(f"Remaining available seats: {item.avail}")

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {processor.sales_value}")
    print("-----------------------------------------------------")
