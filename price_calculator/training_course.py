class TrainingCourse:
    def __init__(self, scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, type, full_price):
        self.scheduled_date = scheduled_date
        self.days_before_training_course = days_before_training_course
        self.total_number_of_seats = total_number_of_seats
        self.remaining_available_seats = remaining_available_seats
        self.online = online
        self.type = type
        self.current_discounted_price = full_price
        self.full_price = full_price
        