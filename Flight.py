'''
Flight
There is a class named Flight, which has the upTime and downTime as the properties. The class should also have a method named calculateFlight, which will return the calculated flying time. You need to complete this method.

Here, upTime denotes the time at which a given bird starts flying, and downTime is the time at which the bird lands somewhere.

You don't need to worry about input/output and object of the class. The given template will take care of it. Also, it is given the bird will fly in the morning, and will land before night of the same day.

The input will contain the upTime and downTime, in 24 hr notation as hh:mm (h is hour, and m is min). You need to calculate the flying time of the given bird (in minutes), as output.

Input
First line contains upTime in the given notation. Second line contains downTime in the given notation.

Output
One Integer denoting the flying time in minutes.

Example
Input1:

10:55
22:55
Output1:

720
Explanation:

Flying time will be 12 hrs = 720 min.
'''
### Define the required class here...

class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime
        

    def calculateFlight(self):
        # Your Code goes here
        down=(60*(int(self.downTime[0])*10+int(self.downTime[1])))+(int(self.downTime[3])*10+int(self.downTime[4]))
        up=(60*(int(self.upTime[0])*10+int(self.upTime[1])))+(int(self.upTime[3])*10+int(self.upTime[4]))
        time=down-up
        return time

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())