from .price_calculator import PriceCalculator
from .training_course_repository import TrainingCourseRepository
from .sales_target_calcaulator import SalesTargetCalculator

class TrainingCourseService:
    def __init__(self, training_courses):
        self.repository = TrainingCourseRepository(training_courses)
        self.price_calculator = PriceCalculator()
        self.sales_target_calculator = SalesTargetCalculator()

    def get_scheduled_training_courses(self):
        return self.repository.get_scheduled_training_courses()

    def get_remaining_sales_target(self):
        return self.sales_target_calculator.get_remaining_sales_target()

    def update_current_prices(self):
        self.price_calculator.update_current_prices(self.repository.get_scheduled_training_courses())

    def update_sales_target(self):
        self.sales_target_calculator.update_sales_target(self.repository.get_scheduled_training_courses())

    def move_to_next_day_before_training_course(self):
        for training_course in self.repository.get_scheduled_training_courses():
            if self.is_before_scheduled_date(training_course):
                training_course.decrease_days_before_training_course()

    def is_before_scheduled_date(self, training_course):
        return training_course.get_days_before_training_course() > 0
    