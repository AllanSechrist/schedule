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
        self.job_duties = ['box', 's/4', 's/3', 'u/2', 'p/5', 'u/1', 'p/6', 'u/p', 'u/p', 'u/p']

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
        job = 0
        print('FOR THE DAY OF ' + self.date)
        for employee in self.opening_shift:
            print("opening:", self.date, employee.name, self.job_duties[job], "Days:", employee.days)
            job += 1
        print()
        job = 0
        for employee in self.closing_shift:
            print("closing:", self.date, employee.name, self.job_duties[job], "Days:", employee.days)
            job += 1
        print()
    """
    def assign_shift_duties(self, shift):
        job = 0
        for employee in shift:
            #employee.assign_job_duty(self.job_duties[job])

            job += 1
            employee.days += 1

    def assign_job_duties(self):
        self.assign_shift_duties(self.opening_shift)
        self.assign_shift_duties(self.closing_shift)
    """
    def add_day(self, shift):
        for employee in shift:
            employee.days += 1

    def add_employee_days(self):
        self.add_day(self.opening_shift)
        self.add_day(self.closing_shift)

class Week(object):
    """
    Manages days and the assignment of duties and scheduling for each day
    """

    def __init__(self, month, year, week):
        self.start_day = 1
        self.month = month
        self.year = year
        self.week = week
        self.list_of_days = []

    # adds day objects to the week
    def add_days(self):
        name = 0
        for x in range(len(self.week)):
            date = str(self.start_day) + self.month + self.year
            #day = Day(date, weekend=False)

            if self.week[name] == 'FRIDAY' or self.week[name] == 'SATURDAY' or self.week[name] == 'SUNDAY':
                day = Day(date, weekend=True)
            else:
                day = Day(date, weekend=False)

            self.list_of_days.append(day)
            self.start_day += 1
            name += 1

    # assigns employees a shift for each day in this week
    def add_workers_to_days(self, list_of_employee_objects):
        for day in self.list_of_days:
            day.add_workers(list_of_employee_objects)
            day.assign_shift()
            day.add_employee_days()
            #day.assign_job_duties()

    # creates the week
    def create_week(self, list_of_employee_objects):
        self.add_days()
        self.add_workers_to_days(list_of_employee_objects)

    # prints out which days and shifts each employee is working
    def get_employees_working(self):
        for day in self.list_of_days:
            day.get_names_of_employees_working()
