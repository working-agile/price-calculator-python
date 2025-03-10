import time
import psycopg2
from .item import Item

class DataProcessor:

    sales_value = 0
    list = []

    _database = None
    _the_singleton = None

    def __new__(cls):
        if cls._the_singleton is None:
            # Simulating a slow initialization process
            time.sleep(1)
            cls._the_singleton = super().__new__(cls)
        return cls._the_singleton

    @staticmethod
    def set_test_connection(test_connection):
        DataProcessor._database = test_connection

    @staticmethod
    def get_instance():
        if DataProcessor._the_singleton is None:
            DataProcessor._the_singleton = DataProcessor()
        return DataProcessor._the_singleton

    def calculate_data(self, next_item):
        if DataProcessor._database is None:
            try:
                url = "dbname='postgres' user='postgres' host='127.0.0.1' password='postgres'"
                DataProcessor._database = psycopg2.connect(url)
            except Exception as e:
                pass

        try:
            query = "SELECT * FROM tr_crs"
            with DataProcessor._database.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                DataProcessor.sales_value = 0
                new_list = []

                for row in rows:
                    id, tr_date, days, ttl_seats, avail, type, curr_price, full_price = row
                    item = Item(id, tr_date, days, ttl_seats, avail, type, curr_price, full_price)

                    if not (item.days < 0 or (next_item and item.days == 0)):
                        new_list.append(item)

                        if next_item:
                            item.days -= 1

                        if item.days <= 10:
                            if item.days <= 1 or (item.avail < 3 and item.days <= 5):
                                item.curr = item.full
                            else:
                                if item.type == "CSD":
                                    item.curr = item.full - (item.days * 30)
                                else:
                                    item.curr = item.full - (item.days * 20)
                        elif item.days > 10:
                            if item.days <= 1 or (item.avail < 3 and item.days <= 5):
                                item.curr = item.full
                            else:
                                if item.type == "CSM":
                                    item.curr = item.full - 500
                                else:
                                    item.curr = item.full - 400

                        if item.type == "CSD" and item.curr < 900:
                            item.curr = 900
                        elif item.type == "CSM" and item.curr < 1000:
                            item.curr = 1000
                        elif item.type == "CSPO" and item.curr < 1200:
                            item.curr = 1200

                        DataProcessor.sales_value += item.avail * item.curr

                DataProcessor.list = new_list

                for item in new_list:
                    update = "UPDATE tr_crs SET days=%s, curr_price=%s WHERE id=%s"
                    with DataProcessor._database.cursor() as update_cursor:
                        update_cursor.execute(update, (item.days, item.curr, item.id))

        except Exception as e:
            print(e)
            pass
