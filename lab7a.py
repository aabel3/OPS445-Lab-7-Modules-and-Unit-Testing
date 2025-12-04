#!/usr/bin/env python3
# OPS445 - Lab 7
# lab7a.py
# Author: Avraham Abel

# Store one IPv4 address
class IPAddress:
    def __init__(self, address):
        self.address = address
        octets = self.address.split(".")
        for octet in octets:
            if not (int(octet) >= 0 and int(octet) < 255):
                print("This (" + octet + ") cannot be an ip address")
            print("octets[0] is " + octets[0])
            if octet == 0:
                print("The first octet cannot be 0")

    def isPrivate(self):
        if self.address.startswith("192.168") or self.address.startswith("10."):
            return True
        else:
            return False

# Store information about a person
class Person:
    def __init__(self, full_name, email=None):
        self.full_name = full_name
        self.email = email
        print("Person name is " + self.full_name)

    def hasEmail(self):
        if self.email:
            print(self.full_name + " has an email: " + self.email)
        else:
            print(self.full_name + " does not have an email")

# Store information about different models from a specific manufacturer
class BMWModel:
    def __init__(self, model_name, seats, fuel_usage, price_range):
        self.model_name = model_name
        self.seats = seats
        self.fuel_usage = fuel_usage
        self.price_range = price_range
        print("Model name is " + self.model_name)

    def isEfficient(self):
        if self.fuel_usage < 7.0:
            print(self.model_name + " is fuel efficient")
        else:
            print(self.model_name + " is not fuel efficient")

# Store information about a specific car that someone owns
class Car:
    def __init__(self, owner, color, model, vin):
        self.owner = owner
        self.color = color
        self.model = model
        self.vin = vin
        print(self.owner + "'s " + self.color + " " + self.model + " with VIN " + self.vin)

    def isValidVIN(self):
        if len(self.vin) == 10 and self.vin.isdigit():
            print("VIN " + self.vin + " is valid")
        else:
            print("VIN " + self.vin + " is not valid")

if __name__ == '__main__':
    # IPAddress objects
    ip1 = IPAddress("192.168.1.3")
    if ip1.isPrivate():
        print("ip1 is on a private subnet")
    else:
        print("ip1 is on a public subnet")

    ip2 = IPAddress("10.0.0.50")
    if ip2.isPrivate():
        print("ip2 is on a private subnet")
    else:
        print("ip2 is on a public subnet")

    ip3 = IPAddress("142.204.1.2")
    if ip3.isPrivate():
        print("ip3 is on a private subnet")
    else:
        print("ip3 is on a public subnet")

    # Person objects
    person1 = Person("Andrew Oatley-Willis", "andrew@example.com")
    person2 = Person("Murray Saul")
    person3 = Person("Andrew Smith", "asmith@school.edu")
    person1.hasEmail()
    person2.hasEmail()
    person3.hasEmail()

    # BMWModel objects
    model1 = BMWModel("BMW2Series", 5, 7.2, "$35,000-$45,000")
    model2 = BMWModel("BMW3Series", 5, 6.8, "$40,000-$55,000")
    model3 = BMWModel("BMW4Series", 4, 7.5, "$45,000-$60,000")
    model4 = BMWModel("BMWXSeries", 7, 9.0, "$50,000-$70,000")
    model5 = BMWModel("BMWMSeries", 5, 10.5, "$60,000-$90,000")
    model6 = BMWModel("BMWiSeries", 5, 0.0, "$45,000-$80,000")
    model2.isEfficient()
    model5.isEfficient()

    # Car objects
    car1 = Car("Andrew", "silver", "Civic", "1234567890")
    car2 = Car("John", "blue", "Subaru", "0987654321")
    car3 = Car("Evan", "black", "BMWMSeries", "4567981230")
    car1.isValidVIN()
    car3.isValidVIN()
