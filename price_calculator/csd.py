from .training_course import TrainingCourse

class CSD(TrainingCourse):
    def __init__(self, scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price):
        super().__init__(scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price)

    def update_current_price(self):
        if self.is_proportional_early_bird():
            self.set_current_discounted_price(self.get_full_price() - (self.get_days_before_training_course() * 30))
        elif self.is_super_early_bird():
            self.set_current_discounted_price(self.get_full_price() - 400)

        if self.get_current_discounted_price() < 900:
            self.set_current_discounted_price(900)

    def get_description(self):
        return "CSD"
    