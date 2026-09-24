from dao.employee_dao import EmployeeDao
class EmployeeService:
    def display_all_employees(self):
        print("Processing Employee Request....")
        dao=EmployeeDao() #dao object dao
        employees=dao.get_all_employee() #dao function call
        return employees #return statement
    
    def add_employee(self, employee):
        print("service adding employee ...")
        dao=EmployeeDao() #dao object dao
        dao.save_employee(employee) #dao function call
    def search_employee_by_id(self,id):
        dao=EmployeeDAO()
        employee=dao.get_employee_by_id(id)
        return employee
    def update_employee_name_by_id(self,name,id):
        dao=EmployeeDAO()
        employee=dao.update_employee_name_by_id(name,id)
        return employee
    def update_employee_salary_by_id(self,salary,id):
            dao=EmployeeDAO()
            employee=dao.update_employee_salary_by_id(salary,id)
            return employee
    def delete_employee_by_id(self,id):
            dao=EmployeeDAO()
            employee=dao.delete_employee_by_id(id)
            return employee