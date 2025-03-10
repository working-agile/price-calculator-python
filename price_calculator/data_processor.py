import time
import psycopg2
from .item import Item
from .training_class_processor import TrainingClassProcessor

class DataProcessor:

    _processor = None
    _database = None
    _the_singleton = None

    def __new__(cls):
        if cls._the_singleton is None:
            # Simulating a slow initialization process
            time.sleep(1)
            cls.init_database_connection()
            cls._the_singleton = super().__new__(cls)
            cls._processor = TrainingClassProcessor()
        return cls._the_singleton

    def init_database_connection():
        if DataProcessor._database is None:
            try:
                url = "dbname='postgres' user='postgres' host='127.0.0.1' password='postgres'"
                DataProcessor._database = psycopg2.connect(url)
            except Exception as e:
                pass

    @staticmethod
    def set_test_connection(test_connection):
        DataProcessor._database = test_connection

    @staticmethod
    def get_instance():
        if DataProcessor._the_singleton is None:
            DataProcessor._the_singleton = DataProcessor()
        return DataProcessor._the_singleton

    def get_list(self):
        return self._processor.get_items()

    def get_sales_value(self):
        return self._processor.get_sales_value()

    def calculate_data(self, next):
        current_training_courses = self.load_training_courses_from_database()
        new_list = self._processor.process_training_courses(next, current_training_courses)
        self.update_training_courses_in_database(new_list)

    def load_training_courses_from_database(self):
        current_training_courses = []
        try:
            query = "SELECT * FROM tr_crs"
            with DataProcessor._database.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

                for row in rows:
                    id, tr_date, days, ttl_seats, avail, type, curr_price, full_price = row
                    item = Item(id, tr_date, days, ttl_seats, avail, type, curr_price, full_price)
                    current_training_courses.append(item)

        except Exception as e:
            pass
    
        return current_training_courses

    def update_training_courses_in_database(self, new_list):
        try:
            for item in new_list:
                update = "UPDATE tr_crs SET days=%s, curr_price=%s WHERE id=%s"
                with DataProcessor._database.cursor() as update_cursor:
                    update_cursor.execute(update, (item.days, item.curr, item.id))
                    
        except Exception as e:
            pass
        