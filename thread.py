import threading

def car(brandName, maxSpeed):
    print('This car is a ', brandName, ' with max speed ', maxSpeed)


if __name__ == "__main__":
        # creating thread
        t1 = threading.Thread(target=car, args=("Toyota", 100,))
        t2 = threading.Thread(target=car, args=("BMW", 200,))

        # starting thread 1
        t1.start()
        # starting thread 2
        t2.start()

        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()

        # both threads completely executed
        print("Done!")