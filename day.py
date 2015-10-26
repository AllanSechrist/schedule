import random

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

    def schedule_opening(self, list_of_employee_objects):
        shifts = 5
        if self.weekend:
            shifts = 7

        while len(self.opening_shift) < shifts:
            self.opening_shift.append(random.sample(list_of_employee_objects, shifts))
