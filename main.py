import employeelist
import employee
import day


list_of_employee_objects = []
id = 1
# constants
# movie theater week starts on friday and ends on thursday
WEEK = ['FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY']




# manages entire program
def main():
    get_month = input("Please enter month in MM format")
    month = "/" + get_month + "/"
    get_year = input("Please enter year in YYYY format")
    year = get_year

    week = day.Week(month, year, WEEK)

    employeelist.list_of_employees.run_it()
    employee.create_employee(employeelist.list_of_employees.list_of_employees, list_of_employee_objects, id)

    for person in list_of_employee_objects:
        print(person.name, " | ID number:", person.id)
    print()

    week.create_week(list_of_employee_objects)

    week.get_employees_working()

    quit()


if __name__ == "__main__":
    main()
