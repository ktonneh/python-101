class Employee:

    def __init__(self,name):
        self.name = name

    name: str
    age: int
    salary: float
    company = "Google"

    def getSalary(self):
        return self.salary
    
    @staticmethod
    def greet():
        print('Hello')