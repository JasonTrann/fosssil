import threading


condition = threading.Condition()
index_in_queue = 0
nums_car_in_list = 0
car_list = []


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
            with condition:
                global index_in_queue
                while self.branchName != car_list[index_in_queue]:
                    condition.wait()

                print('This car is a ', self.branchName, ' with max speed ', self.maxSpeed)
                index_in_queue += 1

                if index_in_queue >= nums_car_in_list:
                    index_in_queue = 0

                condition.notifyAll()


def main():
    global nums_car_in_list, car_list

    toyota = Car('Toyota', 100)
    bmw = Car('BMW', 200)
    car_list = [toyota.branchName, bmw.branchName]
    nums_car_in_list = len(car_list)

    threading.Thread(target=toyota.run).start()
    threading.Thread(target=bmw.run).start()


if __name__ == "__main__":
    main()
