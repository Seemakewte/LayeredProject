from database.connection import Database
from model.employee import Employee
class EmployeeDao:
    def get_all_employee(self): #function
        print("Dao getting employee data... ")
        db=Database() #database object db 
        conn = db.connect() #database function call
        cursor = conn.cursor() #cursor object cursor
        query = "select * from pdemployee1" #query
        cursor.execute(query) #cursor function call
        rows=cursor.fetchall() #cursor function call
        employees=[]
        for row in rows: #for loop
            employee = Employee(row[0], row[1], row[2]) #employee object employee
            employees.append(employee) #append function call
        cursor.close() #cursor function call
        conn.close() #connection function call
        return employees #return statement
    
    def save_employee(self, employee): #function
        print("Dao saving employee data... ")
        print("Employee id:", employee.id)
        print("Employee name:", employee.name)
        print("Employee salary:", employee.salary)
        db=Database() #database object db
        #db.connect() #database function call
        conn = db.connect() #database function call
        cursor = conn.cursor() #cursor object cursor
        query = "insert into pdemployee1(id, name, salary) values(%s, %s, %s)" #query
        data = (employee.id, employee.name, employee.salary) #data tuple
        cursor.execute(query, data) #cursor function call
        conn.commit() #connection function call
        conn.close() #connection function call
        print("Employee data saved successfully pls check!")
    def update_employee_name_by_id(self,name,id):
            db=database()
            conn=db.connect()
            cursor=conn.cursor()
            query='update pdemployee1 set name=%s where id = %s'
            data=(name,id)
            cursor.execute(query,data)
            row=cursor.rowcount
            conn.commit()
            conn.close
            return row
    def update_employee_salary_by_id(self,salary,id):
            db=database()
            conn=db.connect()
            cursor=conn.cursor()
            query='update pdemployee1 set salary = %s where id = %s'
            data=(salary,id)
            cursor.execute(query,data)
            row=cursor.rowcount
            return row
    def delete_employee_by_id(self,id):
            db=database()
            conn=db.connect()
            cursor=conn.cursor()
            query='delete from pdemployee1 where id = %s'
            cursor.execute(query,(id,))
            row=cursor.rowcount
            return row
    
    def get_employee_by_id(self,id):
            db=database()
            conn=db.connect()
            cursor=conn.cursor() 
            query='select * from pdemployee1 where id =%s '
            cursor.execute(query,(id,))   
            row=cursor.fetchone()
            cursor.close()
            conn.close()    
            if row is not None:
                employee=Employee(row[0],row[1],[2])
                return employee
            return None