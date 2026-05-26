import random


class Dice:
    def __init__(self):
        self.nembers = []

    def playDice(self):     # 5회 반복한 값을 리스트에 저장
        self.nembers.append(random.randint(1,6))

    def getNumbers(self):   # 리스트 안의 값을 조회하는 기능
        return self.nembers
    
    def getSum(self):       # 리스트 안의 값을 합하는 기능
        return sum(self.nembers)