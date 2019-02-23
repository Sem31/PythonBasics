class vehicle:
    def __init__(self,speed,cost):
        self.speed = speed
        self.cost = cost
    def pri(self):
        print("speed ",self.speed)
        print("cost : ",self.cost)

print("Bike Details :")
bike = vehicle(80,10000)
bike.pri()
print("car Details :")
car = vehicle(120,1.2)
car.pri()