from behave import given, when, then
from datetime import datetime
from price_calculator import TrainingCourseService, TrainingCourseFactory

def training_course_from_table(data_table):
    data_table = data_table[0].as_dict()
    type_training_course = data_table['training course']
    full_price = int(data_table['full price'])
    scheduled_date_str = data_table['scheduled date']
    current_date_str = data_table['current date']

    scheduled_date = datetime.strptime(scheduled_date_str, '%d/%m/%Y')
    current_date = datetime.strptime(current_date_str, '%d/%m/%Y')

    days_before_training_course = (scheduled_date - current_date).days

    return TrainingCourseFactory.create_training_course(
        type_training_course, scheduled_date_str, days_before_training_course,
        10, 10, True, full_price
    )

@given('the following training course has been scheduled')
def step_given_the_following_training_course(context):
    training_course = training_course_from_table(context.table)
    context.training_courses = [training_course]
    context.service = TrainingCourseService(context.training_courses)

@when('a client checks for the current price')
def step_when_a_client_checks_for_the_current_price(context):
    context.service.update_current_prices()

@then('the discounted price should be {expected_discounted_price:d}')
def step_then_the_discounted_price_should_be(context, expected_discounted_price):
    assert context.training_courses[0].get_current_discounted_price() == expected_discounted_price
