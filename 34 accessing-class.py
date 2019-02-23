class employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    

    def display(self):
        print("name : ",self.name," sal : ",self.sal)

        


emp1 = employee("sem",47000)
emp2 = employee("kamlesh",8000)

emp1.display()
emp2.display()

print("Name (class name) : ",employee.__name__)
print("documentation  : ",employee.__doc__)
print("dictionary : ",employee.__dict__)
print("Module : ",employee.__module__)
print("class : ",employee.__class__)
print("Bases : ",employee.__bases__)


