class ItemProcessor:
    def __init__(self):
        self._sales_value = 0
        self._list = []

    def get_sales_value(self):
        return self._sales_value
    
    def get_list(self):
        return self._list

    def process_items(self, items, advance_day):
        self._sales_value = 0
        processed_items = []

        for item in items:
            self.process_item(advance_day, item, processed_items)

        self._list = processed_items
        return processed_items

    def process_item(self, advance_day, item, new_list):
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

            self._sales_value += (item.avail * item.curr)
