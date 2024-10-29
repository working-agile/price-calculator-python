class PriceCalculator:

    def update_current_prices(self, scheduled_training_courses):
        for training_course in scheduled_training_courses:
            if self.full_price_policy_applies(training_course):
                training_course.set_current_discounted_price(training_course.get_full_price())
            else:
                training_course.update_current_price()

    def full_price_policy_applies(self, training_course):
        return training_course.get_days_before_training_course() <= 1 or (
            training_course.get_remaining_available_seats() < 3 and training_course.get_days_before_training_course() <= 5
        )
    