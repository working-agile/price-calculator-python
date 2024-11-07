from .training_course import TrainingCourse

class ODSF(TrainingCourse):
    def __init__(self, scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price):
        super().__init__(scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price)

    def update_current_price(self):
        pass

    def get_description(self):
        return "OD-SF"

    def decrease_days_before_training_course(self):
        raise RuntimeError("ODSF don't have a scheduled date!")
    