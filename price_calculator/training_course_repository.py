class TrainingCourseRepository:
    def __init__(self, training_courses):
        self.scheduled_training_courses = training_courses

    def get_scheduled_training_courses(self):
        return list(self.scheduled_training_courses)
    