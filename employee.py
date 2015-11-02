class Employee(object):
    """
    creates employee objects
    """

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.days = 0
        self.job_duty = ''


    """
    I discoved that this function does not work as intended
    as the employee object is created only once, each time
    an employee is assigned a new job duty for a new shift
    if overrides self.job_duty and makes it that persons
    job duty for the whole week, job duties must be assigned to
    the shift for each day, for it is the day object that changes
    not the employee object

    def assign_job_duty(self, job_duty):
        self.job_duty = job_duty
    """

class Manager(Employee):
    def __init__(self, name, id):
        Employee.__init__(self, name, id)
        self.manager = True


def create_employee(list_of_names, list_of_objects, id):
    for name in list_of_names:
        employee = Employee(name, id)
        list_of_objects.append(employee)
        id += 1
