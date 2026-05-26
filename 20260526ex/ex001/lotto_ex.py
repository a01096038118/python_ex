import random

userNums = []                    # 사용자가 입력한 난수
randNums = []                    # 랜덤 난수
collect = []                     # 일치하는것 배치

def setUNumbers(ns):                    # setter(데이터를 세팅하는 함수)  set + UNumbers
    #userNums에 아이템을 세팅한다.
    global userNums
    userNums = ns

def getUNumbers():                      # getter   get + UNumbers
    return userNums

def setRNumbers():
    global randNums

    randNums = random.sample(range(1,46),6)
    
def getRNumbers():
    return randNums
    
def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)

    return collect
