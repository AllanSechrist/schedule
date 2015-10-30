import employeelist
import employee
import day

list_of_employee_objects = []
id = 1
start_date = 1
week = day.Week(start_date)

# manages entire program
def main():
    employeelist.list_of_employees.run_it()
    employee.create_employee(employeelist.list_of_employees.list_of_employees, list_of_employee_objects, id)

    # debug
    print(list_of_employee_objects)
    # end debug

    for person in list_of_employee_objects:
        print(person.name, " | ID number:", person.id)

    week.create_week(list_of_employee_objects)

    week.get_employees_working()

    quit()


if __name__ == "__main__":
    main()
