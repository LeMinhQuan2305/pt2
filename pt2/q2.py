import csv
import os

class Employee:
    def __init__(self, code, name, salary, allowance):
        self.code = code
        self.name = name
        self.salary = salary
        self.allowance = allowance

def read_employees(filename):
    employees = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            code, name, salary, allowance = row
            employees.append(Employee(code, name, float(salary), float(allowance)))
    return employees

def write_employees(filename, employees):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for employee in employees:
            writer.writerow([employee.code, employee.name, employee.salary, employee.allowance])

def add_employee(filename, employee):
    employees = read_employees(filename)
    employees.append(employee)
    write_employees(filename, employees)

def binary_search(employees, target_name):
    left, right = 0, len(employees) - 1
    while left <= right:
        mid = (left + right) // 2
        if employees[mid].name == target_name:
            return employees[mid]
        elif employees[mid].name < target_name:
            left = mid + 1
        else:
            right = mid - 1
    return None

def remove_employee(filename, code):
    employees = read_employees(filename)
    for employee in employees:
        if employee.code == code:
            employees.remove(employee)
            write_employees(filename, employees)
            return True
    return False

def sort_employees_by_salary_allowance(employees):
    return sorted(employees, key=lambda x: x.salary + x.allowance, reverse=True)

def main():
    filename = "input.txt"

    while True:
        print("\n1. Add Employee")
        print("2. Find Employee by Name")
        print("3. Remove Employee by Code")
        print("4. Print Employees in Descending Order of Salary + Allowance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter employee code: ")
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            allowance = float(input("Enter employee allowance: "))
            employee = Employee(code, name, salary, allowance)
            add_employee(filename, employee)
            print("Employee added successfully.")

        elif choice == '2':
            target_name = input("Enter name to search: ")
            employees = read_employees(filename)
            result = binary_search(employees, target_name)
            if result:
                print("Employee found:")
                print("Code:", result.code)
                print("Name:", result.name)
                print("Salary:", result.salary)
                print("Allowance:", result.allowance)
            else:
                print("Employee not found.")

        elif choice == '3':
            code = input("Enter employee code to remove: ")
            if remove_employee(filename, code):
                print("Employee removed successfully.")
            else:
                print("Employee not found.")

        elif choice == '4':
            employees = read_employees(filename)
            sorted_employees = sort_employees_by_salary_allowance(employees)
            print("Employees sorted by Salary + Allowance (descending order):")
            for employee in sorted_employees:
                print("Code:", employee.code)
                print("Name:", employee.name)
                print("Salary:", employee.salary)
                print("Allowance:", employee.allowance)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()