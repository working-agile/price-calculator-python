from price_calculator import DataProcessor, TrainingCourse

def test_manual():
    print("Today is: 1. January 2025")
    print("Registering training courses:")

    i1 = TrainingCourse("10 January 2025", 10, 30, 8, True, "CSD", 3000)
    i2 = TrainingCourse("9 January 2025", 9, 30, 7, True, "CSPO", 4000)
    i3 = TrainingCourse("20 January 2025", 20, 30, 27, False, "CSM", 3000)
    training_courses = [i1, i2, i3]

    processor = DataProcessor(training_courses)

    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(False)

    for training_course in processor.get_scheduled_training_courses():
        print("------------------------------")
        print("Training course")
        print(f"Type: {training_course.type}")
        print(f"When: {training_course.scheduled_date}")
        print(f"Remaining days before training course: {training_course.days_before_training_course}")
        print(f"Online: {training_course.online}")
        print(f"Full Price: {training_course.full_price}")
        print(f"Current price: {training_course.current_discounted_price}")
        print(f"Number of seats: {training_course.total_number_of_seats}")
        print(f"Remaining available seats: {training_course.remaining_available_seats}")

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {processor.get_remaining_sales_target()}")
    print("-----------------------------------------------------")

    print("\n\nMove to next day: 2. January")

    processor.move_to_next_day_before_training_course_update_current_prices_of_training_courses_update_sales_target(True)

    print("Registered training courses")

    for training_course in processor.get_scheduled_training_courses():
        print("------------------------------")
        print("Training course")
        print(f"Type: {training_course.type}")
        print(f"When: {training_course.scheduled_date}")
        print(f"Remaining days before training course: {training_course.days_before_training_course}")
        print(f"Online: {training_course.online}")
        print(f"Full Price: {training_course.full_price}")
        print(f"Current price: {training_course.current_discounted_price}")
        print(f"Number of seats: {training_course.total_number_of_seats}")
        print(f"Remaining available seats: {training_course.remaining_available_seats}")

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {processor.get_remaining_sales_target()}")
    print("-----------------------------------------------------")
    