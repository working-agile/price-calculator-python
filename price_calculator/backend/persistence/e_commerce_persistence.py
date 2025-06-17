import psycopg2
from testcontainers.postgres import PostgresContainer

URL_PRODUCTION_DATABASE = "dbname='production_database' user='postgres' host='127.0.0.1' password='postgres'"
postgres = None

def booting_ecommerce_system():
    start_database()
    create_customers_table_if_not_exists()
    create_training_courses()

def start_database():
    global postgres
    postgres = PostgresContainer("postgres:16-alpine")
    postgres.with_exposed_ports(5432)
    postgres.with_bind_ports(5432, 5432)
    postgres.dbname = "production_database"
    postgres.username = "postgres"
    postgres.password = "postgres"
    postgres.start()

def create_customers_table_if_not_exists():
    try:
        conn = psycopg2.connect(URL_PRODUCTION_DATABASE)
        cursor = conn.cursor()

        create_table_query = """
        create table if not exists tr_crs (
            id bigint NOT NULL,
            tr_date varchar(20) not null,
            days integer,
            ttl_seats integer,
            avail integer,
            type char(10),
            curr_price integer,
            full_price integer
        )
        """

        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise RuntimeError(e)

def create_training_courses():
    try:
        conn = psycopg2.connect(URL_PRODUCTION_DATABASE)
        cursor = conn.cursor()

        insert_queries = [
            "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(1,'9 January 2025',9,30,7,'CSPO',4000)",
            "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(2,'10 January 2025',10,30,8,'CSO',3000)",
            "INSERT INTO tr_crs(id,tr_date,days,ttl_seats,avail,type,full_price) VALUES(3,'20 January 2025',20,30,27,'CSM',3000)"
        ]

        for query in insert_queries:
            cursor.execute(query)

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise RuntimeError(e)