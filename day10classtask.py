from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def calculate_years(self):
        return 2025 - self.joining_year
        
    def __str__(self):
        return f"Name: {self.name} joining_year = {self.joining_year} years being joined:{self.calculate_years()} role:{self.role()}"
    @abstractmethod
    def role(self):
        pass
class Customer(User):
    def role(self):
        return "customer"
    
class Vendor(User):
    def role(self):
        return 'vendor'


user1 = Vendor("gokul",2000)
print(user1)