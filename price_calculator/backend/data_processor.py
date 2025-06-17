import psycopg2
from .item import Item
from .item_processor import ItemProcessor

class DataProcessor:
    _database = None
    
    def __init__(self, database_connection=None):
        self.item_processor = ItemProcessor()
        if database_connection:
            DataProcessor._database = database_connection
    
    def get_sales_value(self):
        return self.item_processor.get_sales_value()
    
    def get_list(self):
        return self.item_processor.get_list()
    
    def calculate_data(self, advance_day):
        self.init_database_connection()
        
        items = self.read_items_from_database()
        
        processed_items = self.item_processor.process_items(items, advance_day)
        
        self.update_prices_in_database(processed_items)
    
    def init_database_connection(self):
        if DataProcessor._database is None:
            try:
                url = "dbname='production_database' user='postgres' host='127.0.0.1' password='postgres'"
                DataProcessor._database = psycopg2.connect(url)
            except Exception as e:
                raise RuntimeError(e)
    
    def read_items_from_database(self):
        items = []
        
        try:
            query = "select * from tr_crs"
            cursor = DataProcessor._database.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            for row in rows:
                id, tr_date, days, ttl_seats, avail, type, curr, full = row
                item = Item(id, tr_date, days, ttl_seats, avail, type, curr, full)
                items.append(item)
            cursor.close()
            
            return items
        except Exception as e:
            raise RuntimeError(e)
    
    def update_prices_in_database(self, new_list):
        try:
            for item in new_list:
                update = "update tr_crs set days=%s, curr_price=%s where id=%s"
                cursor = DataProcessor._database.cursor()
                cursor.execute(update, (item.days, item.curr, item.id))
                DataProcessor._database.commit()
                cursor.close()
        except Exception as e:
            raise RuntimeError(e)