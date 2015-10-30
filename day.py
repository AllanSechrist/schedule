import random
import employee

class Day(object):
    """
    creates a day object that will have an array of employees
    Day will have a date, 3 shifts (opening, mid-shift, and closing)
    The Day object will assign job duties based on shift
    """
    # date will be in DD/MM/YYYY format
    def __init__(self, date, weekend=True):
        self.date = date
        self.opening_shift = []
        self.mid_shift = []
        self.closing_shift = []
        self.weekend = weekend
        self.shifts_to_cover = 20

    def remove_from_list(self, copied_to, copied_from):
        for name in copied_to:
            for copy in copied_from:
                if copy == name:
                    copied_from.remove(copy)

    def add_workers(self, list_of_employee_objects):
        if not self.weekend:
            self.shifts_to_cover = 10

        self.opening_shift = random.sample(list_of_employee_objects, self.shifts_to_cover)

    def assign_shift(self):
        self.closing_shift = random.sample(self.opening_shift, int((self.shifts_to_cover / 2)))
        self.remove_from_list(self.closing_shift, self.opening_shift)

    def get_names_of_employees_working(self):
        for employee in self.opening_shift:
            print("opening:", self.date, employee.name)
        for employee in self.closing_shift:
            print("closing:", self.date, employee.name)

class Week(object):

    def __init__(self, start_date):
        self.start_date = start_date
        self.week = 7
        self.list_of_days = []

    def add_days(self):
        for x in range(self.week):
            day = Day(self.start_date, weekend=False)
            self.start_date += 1
            self.list_of_days.append(day)

    def add_workers_to_days(self, list_of_employee_objects):
        for day in self.list_of_days:
            day.add_workers(list_of_employee_objects)
            day.assign_shift()

    def create_week(self, list_of_employee_objects):
        self.add_days()
        self.add_workers_to_days(list_of_employee_objects)

    def get_employees_working(self):
        for day in self.list_of_days:
            day.get_names_of_employees_working()
