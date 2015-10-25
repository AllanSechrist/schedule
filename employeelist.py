class EmployeeList(object):
    """
    creates the employee list object for editing
    """

    def __init__(self, filename):
        self.employee_list = filename
        self.names = ''
        self.names_to_add = ''
        self.names_to_delete = ''
        self.list_of_employees = []

    # method used to read lines in the given file
    # adds names to self.names for editing purposes

    def open_file(self):
        employee_list = open(self.employee_list, 'r')
        self.names = employee_list.readlines()
        employee_list.close()

        print(self.names)

    # takes user input to add or delete a name in the text file
    def get_name(self):
        first_name = input("Employee first name: ").upper()
        last_name = input("Employee last name: ").upper()
        name = (first_name + " " + last_name)
        return name

    # method to add name and address to excel / text file

    def add_employee(self):
        self.open_file()
        self.names_to_add = self.get_name()

        print(self.names_to_add)

        employee_list = open(self.employee_list, 'w')
        employee_list.truncate()

        for name in self.names:
            employee_list.write(name)
        employee_list.write('\n')
        employee_list.write(self.names_to_add)

        employee_list.close()

    # method to remove a name from the file

    def remove_employee(self):
        self.open_file()
        self.names_to_delete = self.get_name()

        employee_list = open(self.employee_list, 'w')
        employee_list.truncate()

        for name in self.names:
            if name != self.names_to_delete + '\n' and name != self.names_to_delete:
                employee_list.write(name)

        employee_list.close()

    # method to print names in the file
    def print_employees(self):
        self.open_file()
        for name in self.names:
            print(name)

    # method to create a loop for user interaction
    # gets input to perform desired action

    def user_choice(self):
        choice = False
        while not choice:
            user_choice = input("What would you like to do?" '\n'
                                "'A' to add an employee" '\n'
                                "'D' to delete an employee" '\n'
                                "'P' to print current employees" '\n'
                                "'Q' to exit" '\n'
                                "input please: ").upper()

            if user_choice == 'A':
                self.add_employee()
                choice = True
            elif user_choice == 'D':
                self.remove_employee()
                choice = True
            elif user_choice == 'P':
                self.print_employees()
                choice = True
            elif user_choice == 'Q':
                self.open_file()
                print("Ending program")
                choice = True
            else:
                print("error in user input, please try again")

    # manages user interaction with file
    def run_it(self):
        done = False
        while not done:
            self.user_choice()

            finished = input("done? Y or N")

            if finished.upper() == "Y":
                done = True
            else:
                done = False

        self.open_file()
        for name in self.names:
            name = name.replace('\n', '')
            self.list_of_employees.append(name)

        print(self.list_of_employees)


list_of_employees = EmployeeList('test.txt')