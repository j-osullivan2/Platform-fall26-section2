class car:
    def __init__(self, color, engine_type, gas_tank,odometer):
        self.color = color
        self.engine_type = engine_type
        self.gas_tank = gas_tank
        self.odometer = odometer
    def __str__(self):
        return("The car is " + self.color + " with a " + self.engine_type + " engine")
    def drive(self):

        if self.engine_type == "4_cylinder":
            self.gas_tank-=3
            self.odometer+=90
        if self.engine_type == "V8":
            self.gas_tank-=4
            self.odometer+=50
        
    def get_gas_tank(self):
        return(self.gas_tank)

    def get_odometer(self):
        return(self.odometer)



car1=car("red","V8",20,90)
car2=car("blue","4_cylinder",15,90)
car3=car("gree","V8",30,200)

print(car1.__str__())
print(car1.get_odometer())
print(car1.get_gas_tank())
print(car1.drive())
print(car1.get_odometer())
print(car1.get_gas_tank())

print(car2.__str__())
print(car2.get_odometer())
print(car2.get_gas_tank())
print(car2.drive())
print(car2.get_odometer())
print(car2.get_gas_tank())