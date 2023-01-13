# class SuperHeroes():
#      def __init__(self, name, superpower):
#         self.name = name
#         self.superpower =superpower

#      def get_superpower(self):
#          print(f"Iam {self.name} and my power is {self.superpower}")

# ironMan =SuperHeroes(
#     name="Iron Man",
#     superpower="Suit"
# )

# ironMan.get_superpower()

class Sensor():
    def __init__(self, name, location, record_date):
        self.name= name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, data, time):
        self.data["data"] = data
        self.data["time"] = time
        print("Data points added successfully ")

    def clear_data(self):
        self.data = {}
        print("Data removed successfully")

import numpy as np

sensor1 = Sensor(
    name="sensor",
    location="Haldia",
    record_date="2023-01-09"
    )

data = np.random.randint(-10, 10, 10)
time = np.arange(10)
# print(data)

sensor1.add_data(
    data=data,
    time=time)
print(sensor1.data)

class Accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")

import numpy as np

acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

acc = Accelerometer(
    name="Acceleromwter",
    location="Haldia",
    record_date="2023-01-09"
    )

acc.add_data(
    data = acc_data,
    time = acc_time
)

print("Acceleration Data:", acc.data)

