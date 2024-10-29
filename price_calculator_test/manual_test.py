from price_calculator import TrainingCourseService, CSD, CSM, CSPO

def test_manual():
    print("Today is: 1. January 2025")
    print("Registering training courses:")

    i1 = CSD("10 January 2025", 10, 30, 8, True, 3000)
    i2 = CSPO("9 January 2025", 9, 30, 7, True, 4000)
    i3 = CSM("20 January 2025", 20, 30, 27, False, 3000)
    training_courses = [i1, i2, i3]

    training_course_service = TrainingCourseService(training_courses)

    training_course_service.update_current_prices()

    for training_course in training_course_service.get_scheduled_training_courses():
        print("------------------------------")
        print("Training course")
        print(f"Type: {training_course.get_description()}")
        print(f"When: {training_course.get_scheduled_date()}")
        print(f"Remaining days before training course: {training_course.get_days_before_training_course()}")
        print(f"Online: {training_course.get_online()}")
        print(f"Full Price: {training_course.get_full_price()}")
        print(f"Current price: {training_course.get_current_discounted_price()}")
        print(f"Number of seats: {training_course.get_total_number_of_seats()}")
        print(f"Remaining available seats: {training_course.get_remaining_available_seats()}")

    training_course_service.update_sales_target()

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {training_course_service.get_remaining_sales_target()}")
    print("-----------------------------------------------------")

    print("\n\nMove to next day: 2. January")

    training_course_service.move_to_next_day_before_training_course()
    training_course_service.update_current_prices()

    print("Registered training courses")

    for training_course in training_course_service.get_scheduled_training_courses():
        print("------------------------------")
        print("Training course")
        print(f"Type: {training_course.get_description()}")
        print(f"When: {training_course.get_scheduled_date()}")
        print(f"Remaining days before training course: {training_course.get_days_before_training_course()}")
        print(f"Online: {training_course.get_online()}")
        print(f"Full Price: {training_course.get_full_price()}")
        print(f"Current price: {training_course.get_current_discounted_price()}")
        print(f"Number of seats: {training_course.get_total_number_of_seats()}")
        print(f"Remaining available seats: {training_course.get_remaining_available_seats()}")

    training_course_service.update_sales_target()

    print("-----------------------------------------------------")
    print(f"Total sales target remaining: {training_course_service.get_remaining_sales_target()}")
    print("-----------------------------------------------------")
    