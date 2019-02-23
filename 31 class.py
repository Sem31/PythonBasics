#class and object


class Add:
    addcount=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Add.addcount+=1
        
    def displaycount():
        print("display count total emp : ",Add.addcount)

    def display(self):
        print("name : ",self.name," salary : ",self.salary)


a1 = Add('sem',5000)
a2 = Add('kamlesh',1500)

a1.display()
a2.display()
  
print("total emp = ",Add.addcount)
Add.displaycount()
