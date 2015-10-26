import employeelist
import employee

list_of_employee_objects = []
id = 1


# manages entire program
def main():
    employeelist.list_of_employees.run_it()
    employee.create_employee(employeelist.list_of_employees.list_of_employees, list_of_employee_objects, id)

    # debug
    print(list_of_employee_objects)
    # end debug

    for person in list_of_employee_objects:
        print(person.name, " | ID number:", person.id)

    quit()


if __name__ == "__main__":
    main()
