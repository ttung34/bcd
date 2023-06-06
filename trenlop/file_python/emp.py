class Person:
    def person_info(self, name, age):
        print("name: ", name, "age: ",age)  
    
    
        


#Parent class
class Company:
    def company_info(self, company_name, company_stress):
        print("Company name: ", company_name,"Company Stress: ", company_stress)
    
   
class Employee(Person, Company):
    def emp_info(self, salary):
        print("Salary: ", salary)
   
#Creare object at EMployee
emp = Employee()
emp.person_info("Tung", 18)
emp.company_info("Viettle","Cau giay")
emp.emp_info(2000)  
emp.hello()    

#Kiểm tra xem class có phải là class con của class cha không

print(issubclass(Employee, Person))

emp.hello()