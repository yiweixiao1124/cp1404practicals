import datetime


class Project:

    def __init__(self, name, start_date, priority, estimate_cost, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d%m%Y").date()
        self.priority = priority
        self.estimate_cost = estimate_cost
        self.completion_percentage = completion_percentage

    def is_complete(self):
        return int(self.completion_percentage) == 100

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.estimate_cost:,.2f}, {self.completion_percentage}"

    def __lt__(self, other):
        return self.priority <= other.priority

    def compare_date(self, input_date):
        input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date
        return self.start_date >= input_date

    def update_percentage(self, value):
        self.completion_percentage = value

    def update_priority(self, value):
        self.priority = value