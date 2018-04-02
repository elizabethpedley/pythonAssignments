class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    
    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        if self.miles < 5:
            print "You can't reverse. You haven't ridden anywhere!"
            return self
        else:
            print 'Reversing'
            self.miles -= 5
            return self

bike1 = Bike('$200', 35)
bike2 = Bike('$600', 42)
bike3 = Bike('$450', 28)

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()



