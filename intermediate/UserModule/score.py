scores = []
def addKor(kor):
    scores.append(kor)


def addEng(eng):
    scores.append(eng)


def addMath(math):
    scores.append(math)


def getTotalScore():
    total = 0
    for score in scores:
        total += score

    return total


def getAvgScore():
    avg = getTotalScore() // len(scores)
    return avg
