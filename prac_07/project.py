import datetime


class Project:

    def __init__(self, name, start_date, priority, estimate_cost, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate_cost = estimate_cost
        self.completion_percentage = completion_percentage

    def is_complete(self):
        return self.completion_percentage >= 100

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate_cost:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority