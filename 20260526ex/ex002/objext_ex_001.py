# 클래스(객체를 만들기 위한 틀(설계도)) 문법

# 붕어빵 클래스
# class FishBread:                 # 클래스 선언
#     # 속성(attribute)
#     def __init__(self, f, b):    #  클래스 속성 정의 
#         self.flour = f           # f,b 매개변수
#         self.bean = b

#     # 기능(function, method)
#     def makeFishBread(self):     # 클래스 기능 정의 
#         print('붕어빵 제조')       # self 매개변수

# # 붕어빵 클래스로부터 객체를 만들어 봅시다.(객체 생성, 딕셔너리)
# myFishBread = FishBread('팥', '밀가루')         # 초기에 생성될때의 값들을 넣어준다.
# friendFishBread = FishBread('호박', '쌀')         
# hisFishBread = FishBread('꿀', '밀가루')

# print(f'내 붕어빵의 속 내용물: {myFishBread.flour}')         # 팥
# print(f'내 붕어빵의 속 내용물: {myFishBread.bean}')          # 밀가루
# print(f'내 붕어빵의 속 내용물: {friendFishBread.flour}')     # 호박
# print(f'내 붕어빵의 속 내용물: {friendFishBread.bean}')      # 쌀
# print(f'내 붕어빵의 속 내용물: {hisFishBread.flour}')        # 꿀
# print(f'내 붕어빵의 속 내용물: {hisFishBread.bean}')         # 밀가루



# 계산기 클래스
# class Calculator:
#     # 속성
#     def __init__(self,n1, n2):
#         self.num1 = n1
#         self.num2 = n2
#     # 기능
#     def add(self):
#         print(f'add: {self.num1 + self.num2}') 

#     def sub(self):
#          print(f'sub: {self.num1 - self.num2}') 

#     def mul(self):
#          print(f'mul: {self.num1 * self.num2}') 

#     def div(self):
#          print(f'div: {self.num1 / self.num2}') 

# myCalculator = Calculator(10, 20)
# friendCalculator = Calculator(100, 200)

# myCalculator.add()       # 30
# myCalculator.sub()       # -10
# myCalculator.mul()       # 200
# myCalculator.div()       # 0.5

# friendCalculator.add()
# friendCalculator.sub()
# friendCalculator.mul()
# friendCalculator.div()


# 인간 클래스 만들기
class Human:
    # 속성
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # 기능
    def walk(self):
        print('걷기')

    def run(self):
        print('달리기')

    def printMyInfo(self):
        print(f'나의 신장: {self.height}')
        print(f'나의 체중: {self.weight}')

human1 = Human(188, 87)
human2 = Human(165, 49)

human1.printMyInfo()
human2.printMyInfo()

human1 =human2
human1.printMyInfo()

human1.height = 200
human1.weight = 39

human2.printMyInfo()

# 라면 클래스
class MyNudle:
    # 속성
    def __init__(self, soup, nudle):
        self.soup = soup
        self.nudle = nudle
    
    # 기능
    def cup(self):
        print('컵라면')
    
    def bag(self):
        print('봉지라면')

    def MakeNudle(self):
        print(f'라면 재료: {self.soup}')
        print(f'라면 재료: {self.nudle}')

myNudleitem = MyNudle('hot_soup','nudle')
friendNudleitem = MyNudle('soup','large_nudle')

myNudleitem.MakeNudle()
friendNudleitem.MakeNudle()


# 휴대폰 클래스
class UserPhone:
    # 속성
    def __init__(self, call, ktalk, game):
        self.calling = call
        self.kakatalk = ktalk
        self.enjoy = game
    # 기능
    def callback(self):
        print('부재중')

    def emoticon(self):
        print('이모티콘')
    
    def multiplay(self):
        print('게임')

    def myphone(self):
        print(f'전화 목록: {self.calling}')
        print(f'k 토크: {self.kakatalk}')
        print(f'폰 게임: {self.enjoy}')

myphoneLilst1 = UserPhone('house', '동기1', 'maplestory')
myphoneLilst2 = UserPhone('bbq', '동기2', 'kartrider')
myphoneLilst3 = UserPhone('bhc', '동기3', 'minecraft')

myphoneLilst1.myphone()
myphoneLilst2.myphone()
myphoneLilst3.myphone()
    

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = (self.width * self.height) /6
        print(f'삼각형 면적: {area}')
    
triangle1 = Triangle(32, 48)

triangle1.getArea()

