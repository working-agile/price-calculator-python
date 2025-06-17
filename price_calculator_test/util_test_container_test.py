import psycopg2
from testcontainers.postgres import PostgresContainer

postgres = PostgresContainer("postgres:16-alpine")
url = None
username = None
password = None

def beforeAll():
    global postgres, url, username, password
    postgres.start()
    url = postgres.get_connection_url()
    username = postgres.username
    password = postgres.password

def afterAll():
    global postgres
    postgres.stop()

def beforeEach():
    print(f"Connection URL: {url}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    
    conn = get_database_connection()
    create_customers_table_if_not_exists(conn)
    clear_database(conn)
    conn.close()

def afterEach():
    conn = get_database_connection()
    clear_database(conn)
    conn.close()

def get_database_connection():
    try:
        return psycopg2.connect(
            host=postgres.get_container_host_ip(),
            port=postgres.get_exposed_port(5432),
            dbname=postgres.dbname,
            user=username,
            password=password
        )
    except Exception as e:
        raise RuntimeError(e)

def clear_database(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tr_crs;")
        conn.commit()
        cursor.close()
    except Exception as e:
        raise RuntimeError(e)

def create_customers_table_if_not_exists(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tr_crs (
                id bigint NOT NULL,
                tr_date varchar(20) NOT NULL,
                days integer,
                ttl_seats integer,
                avail integer,
                type char(10),
                curr_price integer,
                full_price integer
            )
        """)
        conn.commit()
        cursor.close()
    except Exception as e:
        raise RuntimeError(e)
        