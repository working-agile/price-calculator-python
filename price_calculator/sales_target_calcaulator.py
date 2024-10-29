class SalesTargetCalculator:
    def __init__(self):
        self.remaining_sales_target = 0

    def get_remaining_sales_target(self):
        return self.remaining_sales_target

    def update_sales_target(self, scheduled_training_courses):
        self.remaining_sales_target = 0

        for training_course in scheduled_training_courses:
            self.remaining_sales_target += (training_course.remaining_available_seats * training_course.current_discounted_price)
