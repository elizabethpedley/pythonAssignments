class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print 'Fuel: ' + str(self.fuel)
        print 'Milage: ' + str(self.mileage)
        print 'Tax: ' + str(self.tax)
        return self

BMW = Car(12000, '40mph', 'full', '40mpg')