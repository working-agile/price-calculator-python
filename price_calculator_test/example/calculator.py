class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value

    def get_value(self):
        return self.value

    def add(self, amount):
        self.value += amount

    def subtract(self, amount):
        self.value -= amount

    def clear(self):
        self.value = 0
