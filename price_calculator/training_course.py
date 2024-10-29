from abc import ABC, abstractmethod

class TrainingCourse(ABC):
    def __init__(self, scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price):
        self.scheduled_date = scheduled_date
        self.days_before_training_course = days_before_training_course
        self.total_number_of_seats = total_number_of_seats
        self.remaining_available_seats = remaining_available_seats
        self.online = online
        self.current_discounted_price = full_price
        self.full_price = full_price

    def get_scheduled_date(self):
        return self.scheduled_date

    def get_days_before_training_course(self):
        return self.days_before_training_course

    def get_total_number_of_seats(self):
        return self.total_number_of_seats

    def get_remaining_available_seats(self):
        return self.remaining_available_seats

    def get_online(self):
        return self.online

    def get_current_discounted_price(self):
        return self.current_discounted_price

    def get_full_price(self):
        return self.full_price

    def set_current_discounted_price(self, current_discounted_price):
        self.current_discounted_price = current_discounted_price

    # ---------------------------------------------------------------------------

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def update_current_price(self):
        pass

    def is_super_early_bird(self):
        return self.days_before_training_course > 10

    def is_proportional_early_bird(self):
        return self.days_before_training_course <= 10

    def decrease_days_before_training_course(self):
        self.days_before_training_course -= 1
        