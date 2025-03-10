class TrainingClassProcessor:
    def __init__(self):
        self.items = []
        self.sales_value = 0

    def get_sales_value(self):
        return self.sales_value

    def get_items(self):
        return self.items

    def process_training_courses(self, next, current_training_courses):
        self.sales_value = 0
        new_list = []
        for current_item in current_training_courses:
            self.process_training_course(next, current_item, new_list)
        self.items = new_list
        return new_list

    def process_training_course(self, next, item, new_list):
        if not (item.days < 0 or (next and item.days == 0)):
            new_list.append(item)

            if next:
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

            self.sales_value += item.avail * item.curr