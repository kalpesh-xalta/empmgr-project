from .models import make_employee
from .storage import load_employees,save_employees
from .validators import parse_salary
from rich.console import Console
from rich.table import Table

def show_employees(employees):
    table = Table(title="Employees")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Department")
    table.add_column("Saladery")

    for emp in employees:
        table.add_row(
            str(emp["id"]),
            emp["name"],
            emp["department"],
            f"{emp['salary']:,.2f}"
        )

    Console().print(table)

def main():
 employees = load_employees()
 while True:     
        print("\n=== Employee Manager ===") 
        print("1. List employees") 
        print("2. Add employee") 
        print("3. Quit") 
        
        choice = input("Choose an option: ").strip() 
        if choice == "1": 
            show_employees(employees) 
        elif choice == "2": 
            name = input("Name: ").strip() 
            email = input("Email: ").strip() 
            department = input("Department: ").strip() 
            salary = parse_salary(input("Salary: ")) 
            if not name or salary is None: 
                print("Invalid input - employee not added.") 
                continue 
            make_employee(employees, name, email, department, salary) 
            save_employees(employees) 
        elif choice == "3": 
            break 
        else: 
            print("Invalid option.")

if __name__ == "__main__":
    main()