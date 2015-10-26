class Employee(object):
    """
    creates employee objects
    """

    def __init__(self, name, id):
        self.name = name
        self.id = id


class Manager(Employee):
    def __init__(self):
        super(Employee, self).__init__(self)


def create_employee(list_of_names, list_of_objects, id):
    for name in list_of_names:
        employee = Employee(name, id)
        list_of_objects.append(employee)
        id += 1

