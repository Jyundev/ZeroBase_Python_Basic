# 자동차 경주 게임 클래스

class Car:
    def __init__(self, n, c, s):
        self.name = n
        self.color = c
        self.speed = s

    def printCarInfo(self):
        print(f'Car is {self.name}')
        print(f'Color is {self.color}')
        print(f'Speed is {self.speed}')

    def controlSpeed(self, s):
        self.speed = s

    def getDistanceForHour(self, t):
        return self.speed * t


class CarRacing:
    def __init__(self):
        self.car = {}

    def startRacing(self):
        pass

    def printCurrentCarDistance(self):
        pass

    def addCar(self):
        pass


