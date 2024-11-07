from .csd import CSD
from .csm import CSM
from .cspo import CSPO
from .odsf import ODSF

class TrainingCourseFactory:

    @staticmethod
    def create_training_course(course_type, scheduled_date, days_before_training_course,
                               total_number_of_seats, remaining_available_seats, online, full_price):
        if course_type == "CSD":
            return CSD(scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price)
        elif course_type == "CSM":
            return CSM(scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price)
        elif course_type == "CSPO":
            return CSPO(scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price)
        elif course_type == "OD-SF":
            return ODSF(scheduled_date, days_before_training_course, total_number_of_seats, remaining_available_seats, online, full_price)
        else:
            raise ValueError("Unknown training course type")
        