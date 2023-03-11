income = 0
water = 0
electric = 0
gas = 0


def setIncome(i):
    global income
    income = i


def getIncome():
    return income


def setWater(w):
    global water
    water = w


def getWater():
    return water


def setElectric(e):
    global electric
    electric = e


def getElectric():
    return electric


def setGas(g):
    global gas
    gas = g


def getGas():
    return gas


def getUtility():
    bill = {}
    utility = getWater() + getElectric() + getGas()
    utilityPercent = round(utility / getIncome() * 100, 2)
    bill.update({'utility': utility})
    bill.update({'utilityPercent': utilityPercent})

    return bill
