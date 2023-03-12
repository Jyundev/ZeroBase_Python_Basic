# 추상 클래스를 이용해서 한/영, 한/일 사전 만들기
from abc import ABCMeta
from abc import abstractmethod


class AbsDictionary(metaclass=ABCMeta):

    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registWord(self, w1, w2):
        pass

    @abstractmethod
    def removeWord(self, w1):
        pass

    @abstractmethod
    def updateWord(self, w1, w2):
        pass

    @abstractmethod
    def searchWord(self, w1):
        pass

    def printDic(self):
        for k in self.wordDic.keys():
            print(f'{k} : {self.wordDic[k]}')


class KorToEng(AbsDictionary):

    def printDic(self):
        print('Korean to English')
        super().printDic()

    def registWord(self, w1, w2):
        print(f'단어 등록 : {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeWord(self, w1):

        if w1 in self.wordDic.keys():
            print(f'ENG 단어 삭제 : delete {w1}')
            del self.wordDic[w1]
        else:
            print('존재하지 않는 단어입니다.')

    def updateWord(self, w1, w2):
        print(f'ENG 단어 업데이트 : update {w1} to {w2}')
        self.wordDic.update({w1: w2})

    def searchWord(self, w1):
        print(f'{w1}를 번역 중입니다.')
        if w1 in self.wordDic.keys():
            print(f'{w1} -> {self.wordDic[w1]}')


class KorToJpa(AbsDictionary):

    def printDic(self):
        print('Korean to Japanese')
        super().printDic()

    def registWord(self, w1, w2):
        print(f'단어 등록 : {w1} to {w2}')
        self.wordDic[w1] = w2

    def removeWord(self, w1):

        if w1 in self.wordDic.keys():
            print(f'JP 단어 삭제 : delete {w1}')
            del self.wordDic[w1]
        else:
            print('존재하지 않는 단어입니다.')

    def updateWord(self, w1, w2):
        print(f'JP 단어 업데이트 : update {w1} to {w2}')
        self.wordDic.update({w1: w2})

    def searchWord(self, w1):
        print(f'{w1}를 번역 중입니다.')
        if w1 in self.wordDic.keys():
            print(f'{w1} -> {self.wordDic[w1]}')


korea = ['귤', '딸기', '메론', '고구마', '석류']
jp = ['みかん', 'イチゴ', 'メロン', 'さつまいも', 'ザクロ']
eng = ['Tangerines', 'strawberries', 'melon', 'sweet potatoes', 'pomegranate']

ktj = KorToJpa()
kte = KorToEng()

# 단어 등록
for i in range(len(korea)):
    ktj.registWord(korea[i], jp[i])
for i in range(len(korea)):
    kte.registWord(korea[i], eng[i])

# 단어 출력
ktj.printDic()
kte.printDic()

# 단어 삭제
ktj.removeWord('귤')
kte.removeWord('고구마')

# 단어 수정
ktj.updateWord('메론', 'Under inspection')
kte.updateWord('메론', 'Under inspection')

# 단어 검색
ktj.searchWord('석류')
kte.searchWord('석류')

# 단어 출력
ktj.printDic()
kte.printDic()
