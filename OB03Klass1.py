class Engine():
    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')

class Car():
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_Car = Car(Engine())
my_Car.start()
my_Car.stop()
