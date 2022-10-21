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
    
def main():
    x = Switchboard()

    print("Valid commands are :\n1)add (to add a circuit)\n2)show (show all circuits)\n3)turnon x(turn on a specific circuit)\n4)turnoff x (turn off a specific circuit)\n5)set speed x i (set speed of circuit x to i)\n6)clear (clear all circuits)\n7)exit (exit program)\n")

    while True:

        l = input('Enter command : ').split(' ')

        if l[0].lower() == "add":
            x.addcircuit()

        if l[0].lower() == "turnon":
            circuits[int(l[1])-1][1].turnOn()

        if l[0].lower() == "turnoff":
            circuits[int(l[1])-1][1].turnOff()

        if l[0].lower() == "set":
            if (int(l[2])-1) in range(len(circuits)):
                circuits[int(l[2])-1][2].setspeed(int(l[3]))
            else:
                print("Circuit does not exist")

        if l[0].lower() == "clear":
            circuits.clear()

        if l[0].lower() == "show":
            for i in range(len(circuits)):
                print(f"Fan {i+1} is {circuits[i][1].state} and {circuits[i][0].state} with speed set to {circuits[i][2].speed}")

        if l[0].lower() == "exit":
            exit()

        l.clear()
        
if __name__ == '__main__':
    main()

'''
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
'''