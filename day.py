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
        self.closing_shift = random.sample(self.opening_shift, (self.shifts_to_cover / 2))
        self.remove_from_list(self.closing_shift, self.opening_shift)


