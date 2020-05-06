

print('Hello, World!')


# 1. Class
# # test commit
#
#
# class A:
#     def __init__(self):
#         self.name = 'class A'
#
#     def say_your_name(self):
#         print('I am class {}'.format(self.name))
#
#
# object_a = A()
#
# object_a.say_your_name()
#
# print(type(object_a))


# 2. Abstraction

from random import randint

class Sensor:
    def __init__(self):
        self.temp_format = 'C'
        self.value = self.calculate_value()

    def get_value(self):
        return self.calculate_value()

    def set_format(self, temp_format):
        self.temp_format = temp_format

    def calculate_value(self):
        temp = randint(10, 40)
        if self.temp_format == 'C':
            return temp
        elif self.temp_format == 'F':
            return temp * 1.8 + 32

sensor = Sensor()

sensor.set_format('F')
current_value = sensor.get_value()
print(current_value)


# # 3. Encapsulation
# sensor.__calculate_value()

# 4. Inheritance
class UserFriendlySensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def get_value(self):
         return 'Current temperature is {0} degrees of {1}'.format(self.calculate_value(), self.temp_format)


print('Inheritance')
uf_sensor = UserFriendlySensor()

uf_sensor.set_format('F')
current_value = uf_sensor.get_value()
print(current_value)

# 5. Polymorphism
print(uf_sensor.get_value())
print(sensor.get_value())

