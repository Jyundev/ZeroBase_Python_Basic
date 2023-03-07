# class Car:
#     def __init__(self, c, len):
#         self.color = c
#         self.length = len
#
#     def doStop(self):
#         print('STOP!')
#
#     def doStart(self):
#         print('START!')
#
#     def printCarInfo(self):
#         print(f'color : {self.color} length : {self.length}')
#
#
# car = Car('red', 200)
# car.printCarInfo()
import copy
import datetime
import math
import time

# class Plane:
#
#     def __init__(self, country, date):
#         self.country = country
#         self.date = date
#
#     def doFly(self):
#         print('이륙합니다')
#
#     def doArrive(self):
#         print('착륙합니다')
#
#     def printInfo(self):
#         self.doFly()
#         print(f'이번 여행지는 {self.country} 입니다 ')
#         print(f'오늘 날짜는 {self.date} 입니다 ')
#         self.doArrive()
#
#
# plane = Plane('CANADA', datetime.datetime.now())
# plane.printInfo()

# class NewGenerationPc:
#
#     def __init__(self, name, cpu, memory, ssd):
#         self.name = name
#         self.cpu = cpu
#         self.memory = memory
#         self.ssd = ssd
#
#     def doExcel(self):
#         print('Excel RUN ! ')
#
#     def doPyCharm(self):
#         print('DO Python ! ')
#
#     def printInfo(self):
#         print(f'name : {self.name}')
#         print(f'cpu : {self.cpu}')
#         print(f'memory : {self.memory}')
#         print(f'ssd : {self.ssd}')
#
#
# myPc = NewGenerationPc('myPc', 'i5', '16G', '250G')
# myPc.doExcel()
# myPc.doPyCharm()
# myPc.printInfo()
# print('-' * 20)
# myPc.name = 'New PC'
# myPc.printInfo()

# class Robot:
#     def __init__(self, color, height, weight):
#         self.color = color;
#         self.height = height
#         self.weight = weight
#
#     def printRobotInfo(self):
#         print(f'color : {self.color}')
#         print(f'weight : {self.weight}')
#         print(f'height : {self.height}')
#
#
# rb1 = Robot('red', 200, 80)
# rb2 = Robot('blue', 300, 120)
# rb3 = rb1  # rb3과 rb1의 주소가 같아, 메모리 주소가 copy 됨
#
# rb1.printRobotInfo()
# rb2.printRobotInfo()
# rb3.printRobotInfo()
#
# rb1.color = 'green'
# rb1.height = 400
# rb1.weight = 150
#
# rb1.printRobotInfo()
# rb2.printRobotInfo()
# rb3.printRobotInfo()
#
# scores = [int(input('국어 점수 : ')),
#           int(input('영어 점수 : ')),
#           int(input('수학 점수 : '))]
# copy = scores.copy()
#
# for idx, score in enumerate(scores):  # enumerate : 인덱스와 원소 동시 접근
#
#     copy[idx] = math.trunc(copy[idx] * 1.1)
#     copy[idx] = 100 if copy[idx] > 100 else copy[idx]
#
# print(scores)
# print(copy)
#
# print(f'이전 평균 : {round(sum(scores) / len(scores), 2)}')
# print(f'이후 평균 : {round(sum(copy) / len(copy), 2)}')
#
# class TemCls:
#     def __init__(self, n, s):
#         self.number = n
#         self.str = s
#
#     def printClsInfo(self):
#         print(f'self.number : {self.number}')
#         print(f'self.str : {self.str}')
#

# # 얕은 복사
# tc1 = TemCls(10, 'Hello')
# tc2 = tc1
#
# tc1.printClsInfo()
# tc2.printClsInfo()
#
# tc2.number = 3.14
# tc2.str = 'Bye'
#
# tc1.printClsInfo()
# tc2.printClsInfo()
#
# # 깊은 복사
#
#
# tc1 = TemCls(10, 'Hello')
# tc2 = copy.copy(tc1)
#
# tc2.number = 3.14
# tc2.str = 'bye'
#
# tc1.printClsInfo()
# tc2.printClsInfo()

# scores = [9, 8, 5, 7, 6, 10]
# scoresCopy = []

# scoresCopy = scores
# print(f'id(scores : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# 깊은 복사 1
# for s in scores:
#     scoresCopy.append(s)
#
# # print(f'id(scores):{id(scores)}')
# # print(f'id(scores):{id(scoresCopy)}')  # id 값이 달라짐
#
# # 깊은 복사 2
# scoresCopy.extend(scores)
#
# print(f'id(scores):{id(scores)}')
# print(f'id(scores):{id(scoresCopy)}')  # id 값이 달라짐
#
# # 깊은 복사 3
# scoresCopy = scores.copy()
#
# # 깊은 복사 4
# scoresCopy = scores[:]

# playerScore = [8.1, 9.3, 7.8, 7.6, 8.4, 9.1]
# copyScore = []
# copyScore.extend(playerScore)
#
# copyScore.sort()
# copyScore.pop(0)
# copyScore.pop()
#
# print(f'원본 : {playerScore}')
# print(f'사본 : {copyScore}')
# print(f'원본 평균 : {round(sum(playerScore) / len(playerScore), 2)}')
# print(f'사본 평균 : {round(sum(copyScore) / len(copyScore), 2)}')

# class NormalCar:
#
#     def drive(self):
#         print('[NormalCar drive() called!')
#
#     def back(self):
#         print('[NormalCar back() called!')
#
#
# class TurboCar(NormalCar):
#
#     def turbo(self):
#         print('[TurboCar] turbo called!')
#
#
# myTurbo = TurboCar()
# myTurbo.turbo()
# myTurbo.drive()
# myTurbo.back()
#
#

# class SuperCalculator:
#     def add(self, n1, n2):
#         return print(n1 + n2)
#
#     def sub(self, n1, n2):
#         return print(n1 - n2)
#
#
# class ChildCalculator(SuperCalculator):
#     def mul(self, n1, n2):
#         return print(n1 * n2)
#
#     def div(self, n1, n2):
#         return print(n1 / n2)
#
#
# child = ChildCalculator()
#
# child.mul(15, 5)
# child.div(15, 5)
# child.add(15, 5)
# child.sub(15, 5)

# class Calculator:
#
#     def __init__(self, n1, n2):
#         print('Calculator 생성자 호출')
#         self.num1 = n1
#         self.num2 = n2
#
#
# cal = Calculator(10, 20)
# print(f'num1 : {cal.num1}\tnum2 : {cal.num2}')

# class Parents:
#     def __init__(self, pNum1, pNum2):
#         print('Parents Class Init()')
#
#         self.pNum1 = pNum1
#         self.pNm2 = pNum2
#
#
# class Child(Parents):
#     def __init__(self, cNum1, cNum2):
#         print('Child Class Init()')
#
#         # Parents.__init__(self, cNum1, cNum2)
#         super().__init__(cNum1, cNum2)
#
#         self.cNum1 = cNum1
#         self.cNum2 = cNum2
#
#
# child = Child(23, 15)

# class MidExam:
#     def __init__(self, korMid, engMid, mathMid):
#         self.korMid = korMid
#         self.engMid = engMid
#         self.mathMid = mathMid
#
#
# class FinalExam(MidExam):
#
#     def __init__(self, korMid, engMid, mathMid, korFinal, engFinal, mathFinal):
#         self.korFinal = korFinal
#         self.engFinal = engFinal
#         self.mathFinal = mathFinal
#         super().__init__(korMid, engMid, mathMid)
#         self.scores = [self.korMid, self.engMid, self.mathMid, self.korFinal, self.engFinal, self.mathFinal]
#
#     def getTotal(self):
#         return sum(self.scores)
#
#     def getAvg(self):
#         return round(self.getTotal() / len(self.scores), 2)
#
#
# exam = FinalExam(int(input('중간 국어 : ')), int(input('중간 영어 : ')), int(input('중간 수학 : ')),
#                  int(input('기말 국어  : ')), int(input('기말 영어 : ')), int(input('기말 수학 : ')))
#
# print(f'총점 : {exam.getTotal()}')
# print(f'평균 : {exam.getAvg()}')

# class Car01:
#     def drive(self):
#         print('drive method called()')
#
#
# class Car02:
#     def turbo(self):
#         print('turbo method called()')
#
#
# class Car03:
#     def fly(self):
#         print('fly method called()')
#
#
# class Car(Car01, Car02, Car03):
#     def __init__(self):
#         pass
#
#
# myCar = Car()
# myCar.drive()
# myCar.fly()
# myCar.turbo()

# class Robot:
#     def __init__(self, c, h, w):
#         self.color = c
#         self.height = h
#         self.width = w
#
#     def fire(self):
#         print('미사일 발사!')
#
#     def printInfo(self):
#         print(f'color : {self.color}')
#         print(f'width : {self.width}')
#         print(f'height : {self.height}')
#
#
# class NewRobot(Robot):
#     def __init__(self, c, h, w):
#         super().__init__(c, h, w)
#
#     def fire(self):
#         print('미사일 발사 중지!')
#
#
# myRobot = NewRobot('red', 200, 300)
# myRobot.printInfo()
# myRobot.fire()
#
# class TriangleArea:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def printInfo(self):
#         print(f'width : {self.width}')
#         print(f'height : {self.height}')
#
#     def getArea(self):
#         print('삼각형 넓이 : ', end='')
#         return self.width * self.height / 2
#
#
# class CustomArea(TriangleArea):
#     def __init__(self, w, h):
#         super().__init__(w, h)
#
#     def getArea(self):
#         return str(super().getArea()) + 'c㎡'
#
#
# area = CustomArea(15, 16)
# print(area.getArea())

# from abc import ABCMeta
# from abc import abstractmethod
#
#
# class AirPlane(metaclass=ABCMeta):
#     @abstractmethod
#     def flight(self):
#         pass
#
#     def forward(self):
#         print('전진')
#
#     def backward(self):
#         print('후진')
#
#
# class AirLine(AirPlane):
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 400km/h 비행')
#
#
# class fighterPlane(AirPlane):
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 700km/h 비행')
#
#
# al = AirLine('red')
# al.flight()
#
# fl = fighterPlane('red')
# fl.flight()

from abc import ABCMeta
from abc import abstractmethod


class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass


class DevelopCalculator(Calculator):

    def add(self, n1, n2):
        print(f'{n1} + {n2} : {n1 + n2}')

    def sub(self, n1, n2):
        print(f'{n1} - {n2} : {n1 - n2}')

    def mul(self, n1, n2):
        print(f'{n1} * {n2} : {n1 * n2}')

    def div(self, n1, n2):
        print(f'{n1} / {n2} : {n1 / n2}')


devCal = DevelopCalculator()
devCal.add(10, 20)
devCal.sub(10, 20)
devCal.mul(10, 20)
devCal.div(10, 20)
