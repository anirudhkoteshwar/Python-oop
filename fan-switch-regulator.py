circuits = []
count = 0

class Fan:
    def __init__(self):
        self.state = "Not Spinning"
        self.speed = 0
        self.switch = False

    def start(self):
        if self.switch and self.speed > 0:
            self.state = "Spinning"
    
    def stop(self):
        self.state = "Not Spinning"
    
class Regulator:
    def __init__(self,fan : Fan):
        self.speed = 0
        self.fan = fan
    
    def setspeed(self,s : int):
        if s in range(1,6):
            self.speed = s
            self.fan.speed = s
            self.fan.start()
        elif s == 0:
            self.speed = s
            self.fan.stop()
        else:
            print(f"Invalid speed {s}")
        
class Switch:
    def __init__(self,fan : Fan):
        self.state = "Off"
        self.fan = fan
    
    def turnOn(self):
        self.state = "On"
        self.fan.switch = True
        self.fan.start()

    def turnOff(self):
        self.state = "Off"
        self.fan.switch = False
        self.fan.stop()

class Switchboard:
    def addcircuit(self):
        a = Fan()
        b = Switch(a)
        c = Regulator(a)
        global count 
        count += 1
        global circuits
        circuits.append([a,b,c])
    


x = Switchboard()
x.addcircuit()
circuits[0][1].turnOn()
circuits[0][2].setspeed(3)
print(f"Fan {1} is {circuits[0][1].state} and {circuits[0][0].state} with speed set to {circuits[0][2].speed}")
x.addcircuit()
circuits[1][1].turnOn()
circuits[1][2].setspeed(1)
circuits[0][1].turnOff()
print(f"Fan {1} is {circuits[0][1].state} and {circuits[0][0].state} with speed set to {circuits[0][2].speed}")
print(f"Fan {2} is {circuits[1][1].state} and {circuits[1][0].state} with speed set to {circuits[1][2].speed}")
circuits[1][2].setspeed(0)
print(f"Fan {2} is {circuits[1][1].state} and {circuits[1][0].state} with speed set to {circuits[1][2].speed}")
