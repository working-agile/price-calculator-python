class DataProcessor:

    def __init__(self, training_courses):
        self.remaining_sales_target = 0
        self.scheduled_training_courses = training_courses

    def get_scheduled_training_courses(self):
        return self.scheduled_training_courses[:]

    def get_remaining_sales_target(self):
        return self.remaining_sales_target

    def move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(self, move_to_next_day):

        self.remaining_sales_target = 0

        for training_course in self.scheduled_training_courses:

            if self.is_before_scheduled_date(training_course) and move_to_next_day:
                training_course.days_before_training_course -= 1

            if self.is_proportional_early_bird(training_course):
                if self.full_price_policy_applies(training_course):
                    training_course.current_discounted_price = training_course.full_price
                else:
                    if training_course.type == "CSD":
                        training_course.current_discounted_price = training_course.full_price - (training_course.days_before_training_course * 30)
                    else:
                        training_course.current_discounted_price = training_course.full_price - (training_course.days_before_training_course * 20)

            elif self.is_super_early_bird(training_course):

                if self.full_price_policy_applies(training_course):
                    training_course.current_discounted_price = training_course.full_price
                else:
                    if training_course.type == "CSM":
                        training_course.current_discounted_price = training_course.full_price - 500
                    else:
                        training_course.current_discounted_price = training_course.full_price - 400

            if training_course.type == "CSD" and training_course.current_discounted_price < 900:
                training_course.current_discounted_price = 900
            elif training_course.type == "CSM" and training_course.current_discounted_price < 1000:
                training_course.current_discounted_price = 1000
            elif training_course.type == "CSPO" and training_course.current_discounted_price < 1200:
                training_course.current_discounted_price = 1200

            self.remaining_sales_target += (training_course.remaining_available_seats * training_course.current_discounted_price)

    def full_price_policy_applies(self, training_course):
        return training_course.days_before_training_course <= 1 or (training_course.remaining_available_seats < 3 and training_course.days_before_training_course <= 5)

    def is_before_scheduled_date(self, training_course):
        return training_course.days_before_training_course > 0

    def is_super_early_bird(self, training_course):
        return training_course.days_before_training_course > 10

    def is_proportional_early_bird(self, training_course):
        return training_course.days_before_training_course <= 10
    