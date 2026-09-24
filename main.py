from model import employee
from service.employee_service import EmployeeService
from model.employee import Employee
print("Wellcome to our project!")
service=EmployeeService() #service object service
service.display_all_employees() #service function call
employee = Employee(1237, "chiku", 60000)
service.add_employee(employee) #service function call


employees=service.display_all_employees() #service function call
for employee in employees:
  print("Employee id:", employee.id)
  print("Employee name:", employee.name)
  print("Employee salary:", employee.salary)
  print("-----------------------------")

id = int(input("enter employee id you want to search"))

employee=service.search_employee_by_id(id)
if employee is None:
    print("employee not found")
else:
    print("id = ",employee.id)
    print("name = ",employee.name)
    print("salary = ",employee.salary)

id=int(input("enter the id of employee to update name :"))
name=input("enter the name of the employee :")
employee=service.update_employee_name_by_id(name,id)
if employee is None :
    print("employee not found")
else:
    print("data updated")

id=int(input("enter the id of employee to update name :"))
salary=input("enter the new salary of the employee :")
employee=service.update_employee_salary_by_id(salary,id)
if employee is None :
    print("employee not found")
else:
    print("data updated")

id=int(input("enter the id of employee to delete employee :"))
employee=service.delete_employee_by_id(id)
if employee is None :
     print("employee not found")
else:
     print("data updated")