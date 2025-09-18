class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print(f"""name = {self.name}
age = {self.age}""")

class employee(person):
    def __init__(self,name,age,employee_id):
        person.__init__(self,name, age)
        self.employee_id =employee_id

    def show_details(self):
        print(f"""name = {self.name}
        age = {self.age}
employee id = {self.employee_id}""")
        
class parttime(person):
    def __init__(self,name,age,working_hours):
        person.__init__(self,name,age)
        self.working_hours = working_hours
    def show_details(self):
        print(f"""name = {self.name}
        age = {self.age}
working hours = {self.working_hours}""")

class consultan(employee,parttime):
    def __init__(self,name,age,employee_id,working_hours,project_name):
        employee.__init__(self,name,age,employee_id)
        parttime.__init__(self,name,age,working_hours)
        self.project_name = project_name
    def show_details(self):
        print(f"""name = {self.name}
age = {self.age}
employee id = {self.employee_id}
working hours = {self.working_hours}
peoject_name = {self.project_name}""")

cons = consultan("hiba",21,1001,12.00,"python class") 
cons.show_details()

partti = parttime("gokul",21,12.00) 
partti.show_details()

emp = employee("amal",21,101) 
emp.show_details()

per = person("karthi",21)
per.show_details()
