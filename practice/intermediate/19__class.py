# 자동차 경주 게임 클래스
import random
from time import sleep


class Car:
    def __init__(self, n='Formula', c='black', s=200):
        self.name = n
        self.color = c
        self.maxSpeed = s
        self.distance = 0

    def printCarInfo(self):
        print(f'Car is {self.name}')
        print(f'Color is {self.color}')
        print(f'Max Speed is {self.maxSpeed}')

    def controlSpeed(self):
        return random.randint(0, self.maxSpeed)

    def getDistanceForHour(self):
        return self.controlSpeed() * 1


class CarRacing:
    def __init__(self):
        self.cars = []

    def startRacing(self):
        for i in range(10):
            print(f'Racing : {i + 1}바퀴')
            for car in self.cars:
                car.distance += car.getDistanceForHour()
                sleep(0.3) #딜레이
            self.printCurrentCarDistance()
            print()

    def printCurrentCarDistance(self):
        for car in self.cars:
            print(f'{car.name} : {car.distance} \t\t ', end='')

    def addCar(self, car):
        self.cars.append(car)


car1 = Car()
car2 = Car('Grand', 'green', 300)
car3 = Car('Sports', 'red', 250)
car4 = Car('Stock', 'gray', 150)
car5 = Car('Touring', 'blue', 280)

racing = CarRacing()
racing.addCar(car1)
racing.addCar(car2)
racing.addCar(car3)
racing.addCar(car4)
racing.addCar(car5)

racing.startRacing()
