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

acc = Accelerometer(
    name="Acceleromwter",
    location="Haldia",
    record_date="2023-01-09"
    )





# print("Acceleration Data:", acc.data)

import numpy as np

acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")

gyro_data = np.random.randint(-15, 15, 10)
gyro_time = np.arange(10)

gyro = Gyro(
    name="Gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)

gyro.add_data(time=gyro_time, data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()

# print("ckjkd", gyro.show_sensor_type())
# print("Acceleration Data:", acc.data)


# GPS attribute
# name location
# record_date
# brand
class GPS(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(
            name, location, record_date
        )
        self.brand = brand

gps = GPS(
    name="GPS",
    location="mumbai",
    record_date="2023-01-10",
    brand="espressif"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
