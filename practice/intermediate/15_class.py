class NormalTv:

    def __init__(self, inch=32, color='black', res='full-HD'):
        self.inch = inch
        self.color = color
        self.resolution = res
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):
        print('Turn On')

    def turnOff(self):
        print('Turn Off')

    def printTvInfo(self):
        print(f'TV SIZE : {self.inch} ')
        print(f'TV COLOR : {self.color} ')
        print(f'TV RESOLUTION : {self.resolution} ')
        print(f'SMART TV : {self.smartTv} ')
        print(f'AI TV : {self.aiTv} ')


class Tv4K(NormalTv):

    def __init__(self, i, c, r='4k'):
        super().__init__(i, c, r)

    def setSmartTv(self, smart):
        self.smartTv = smart


class Tv8K(NormalTv):

    def __init__(self, i, c, r='8k'):
        super().__init__(i, c, r)

    def setSmartTv(self, smart):
        self.smartTv = smart

    def setAiTv(self, ai):
        self.aiTv = ai


normal = NormalTv()
normal.printTvInfo()
print('-' * 20)
tv4 = Tv4K(64, 'blue')
tv4.setSmartTv('On')
tv4.printTvInfo()
tv4.turnOn()
print('-' * 20)
tv8 = Tv8K(128, 'red')
tv8.setAiTv('On')
tv8.setSmartTv('On')
tv8.printTvInfo()
tv8.turnOff()