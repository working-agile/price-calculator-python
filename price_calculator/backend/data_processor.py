import psycopg2
from .item import Item

class DataProcessor:
    
    def __init__(self):
        self.sales_value = 0
        self.list = []
        self.database = None

    def calculate_data(self, advance_day):
        if self.database is None:
            try:
                url = "dbname='production_database' user='postgres' host='172.17.0.1' password='postgres'"
                self.database = psycopg2.connect(url)
            except Exception as e:
                raise RuntimeError(e)

        # Read the prices from database
        try:
            query = "select * from tr_crs"
            cursor = self.database.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            self.sales_value = 0
            new_list = []
            
            for row in rows:
                id, tr_date, days, ttl_seats, avail, type, curr, full = row
                item = Item(id, tr_date, days, ttl_seats, avail, type, curr, full)
                
                if not (item.days < 0 or (advance_day and item.days == 0)):
                    new_list.append(item)
                    
                    if advance_day:
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
                    
                    self.sales_value += (item.avail * item.curr)
            
            cursor.close()
            
            # Update prices in database
            for item in new_list:
                update = "update tr_crs set days=%s, curr_price=%s where id=%s"
                cursor = self.database.cursor()
                cursor.execute(update, (item.days, item.curr, item.id))
                self.database.commit()
                cursor.close()
                
            self.list = new_list
            
        except Exception as e:
            print(e)
            pass
