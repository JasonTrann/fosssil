import os

# Create an object from the 'Car' class by passing style and color
class Car:
    # Class attribute
    wheels = 4
    doors = 4
    seats = 5

    # Initializer with instance attributes
    def __init__(self, branchName, maxSpeed):
        self.branchName = branchName
        self.maxSpeed = maxSpeed

    # Method run()
    def run(self):
            for i in range(10):
                print('This car is a ', self.branchName, ' with max speed ', self.maxSpeed)

    def info(self):
        print('This car is a ', self.branchName, ' with max speed ', self.maxSpeed)
        print('Number of wheels', self.wheels, 'Number of seats', self.seats, 'Number of doors', self.doors)
def main():

    toyota = Car('Toyota', 100)
    bmw = Car('BMW', 200)

    toyota.run()
    bmw.run()

    toyota.info()
    bmw.info()

if __name__=="__main__":
    main()


