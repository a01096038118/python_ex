# # quiz) 369 게임 만들기
# '''
# 친구들끼리 많이 하는 369 게임을 만들어보자
# 1부터 99까지 1씩 증가하면서 숫자에 3, 6, 9가 들어 있을때마다 숫자와 함께
# '짝!'을 출력합니다.
# 33 -> 짝!짝!
# '''
# for num in range(1, 100):

#     if num <= 9 :             # 1의 단위            # 중첩 조건 문자
#         if num % 3 == 0:
#             # print(f'{num}: 짝!')
#             print(num, '짝!',end='')
#         else:
#             print(num, end='')
#     else:                     # 10의 단위
       
#         # print(f'{num}')     # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
#         # printStr = str(num)
#         print(num, end='')

#         firstNum = num // 10     # 15 > 15 // 10 -> 1
#         secondNum = num  % 10    # 15 > 15 % 10 -> 5

#         if firstNum % 3 == 0:
#             # print(f'짝!')
#             # printStr += ',짝!'
#             print(', 짝!', end='')

#         if secondNum % 3 == 0 and secondNum != 0:   # 3의 배수이면서 0이 아니여야함
#             # print(f'짝!')
#             # printStr += ',짝!'
#             print(', 짝!', end='')
          
#     print()

# 열차 교차 시간 알아내기
# '''
# 대전역에는 3개 노선의 열차가 오전 9시부터 오후 6시까지 교차 운행한다.
# 3대의 열차가 교차하는 시간을 구해 열차 충돌 사고를 막으세요.
# (단 매일 오전 9시에 대전역에서 모든 열차가 출발한다.)
# ------------------------------------------------------------------
# A열차 : 첫 차 오전 9시      |  마지막 차 오후 6시      |  운행 간격 10분

# B열차 : 첫 차 오전 9시      |  마지막 차 오후 6시      |  운행 간격 25분

# C열차 : 첫 차 오전 9시      |  마지막 차 오후 6시      |  운행 간격 30분
# ------------------------------------------------------------------
# '''
# trainA = 10
# trainB = 25
# trainC = 30

# for n in range(1,541):      # 9시간 * 60분
#     if n % trainC == 0 and n % trainA == 0:    # A 와 B 충돌
#         print('trainC < - > trainA')
#         # print(9 + n//60, end = '')       # 시, n//60 - > n을 60(시간)으로 나눔
#         # print('시', end = '')
#         # print(n % 60, end = '')          # 분
#         # print('분')
#         print(f'{9 + n // 60 }시 {'00' if n % 60 == 0 else n}분')
#     elif n % trainA == 0 and n % trainB == 0:    # A 와 B 충돌
#         print('trainA < - > trainB')
#         # print(9 + n//60, end = '')       # 시, n//60 - > n을 60(시간)으로 나눔
#         # print('시', end = '')
#         # print(n % 60, end = '')          # 분
#         # print('분')
#         print(f'{9 + n // 60 }시 {'00' if n % 60 == 0 else str(n % 60)}분')
#     elif n % trainB == 0 and n % trainC == 0:    # A 와 B 충돌
#         print('trainB < - > trainC')
#         # print(9 + n//60, end = '')       # 시, n//60 - > n을 60(시간)으로 나눔
#         # print('시', end = '')
#         # print(n % 60, end = '')          # 분
#         # print('분')
#         print(f'{9 + n // 60 }시 {'00' if n % 60 == 0 else str(n % 60)}분')
#     elif n % trainC == 0 and n % trainA == 0:    # A 와 B 충돌
#         print('trainC < - > trainA')
#         # print(9 + n//60, end = '')       # 시, n//60 - > n을 60(시간)으로 나눔
#         # print('시', end = '')
#         # print(n % 60, end = '')          # 분
#         # print('분')
#         print(f'{9 + n // 60 }시 {'00' if n % 60 == 0 else str(n % 60)}분')

# quiz) 로그인 기능 만들기
# '''
# 시스템 관리자(administrator) 로그인 기능을 만들어 봅시다.
# 관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렸다면 '암호를 다시 입력하세요!'를 출력하고
# 다시 암호를 물어봅니다.
# 5회 이상 로그인에 실패하면 '로그인 실패!! 횟수 초과!!!' 메세지를 출력하고 종료합니다.
# 암호가 올바르다면 '로그인 성공'을 출력하고 종료합니다. 올바른 암호는 'dwac1234'입니다.
# '''

# ADMIN_PW = 'dw1234'
# count = 1
# while True:
#     if count > 5:
#         print('로그인 실패')
#         break

#     inputPw = input('비밀번호 입력: ')
#     if inputPw != ADMIN_PW:
#         print('x --> 비밀번호를 다시 입력하세요.')
#         count += 1

#     elif inputPw == ADMIN_PW:
#         print('o --> 로그인 성공')
#         break

# quiz) 팩토리얼 만들기
# '''
# 사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램을 만드시오.
# 팩토리얼(factorial, !) n!은 1부터 양의 정수 n까지의 모든 정수를 곱한 값을 말한다.
# (예를 들어, 4!은 1x2x3x4 =24이다.)
# '''
# useInputIntegerData = int(input('양수입력: '))
# result = 1
# for num in range(1, useInputIntegerData +1):
#     result *= num
# print(f'{useInputIntegerData}의 팩토리얼은 {result}다. ')

# quiz) 숫자 맞추기 게임 만들기
'''
0부터 100 사이의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 계속해서 물어보는 게임을 만드시오.
다음은 프로그램 개발에 필요한 요구사항이다.
--- 요구사항 ---
- 1부터 100까지의 난수를 발생시킨다.
- 사용자가 입력한 숫자가 난수와 일치하면 ‘정답입니다.’를 출력하고 게임을 종료한다.
- 사용자가 입력한 숫자가 난수와 일치하지 않으면 ‘틀렸습니다. 다시 입력하세요.’를 출력하고, 다시 물어본다.
- 기회는 10회로 제한한다. 만약 열 번을 넘어가면 ‘게임에 졌습니다.’를 출력하고 게임을 종료한다.
- 사용자가 틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다. 
- 게임이 종료하기 전 난수를 출력한다.
'''
# import random
# randomNum = random.randint(1, 100)

# userNum = int(input('1~100의 숫자를 입력하세요. '))
# count = 1
# while True:
#     if randomNum == userNum:
#         print('정답입니다.')
#         break

#     elif randomNum < userNum:
#         print('틀렸습니다. 다시 입력하세요.DOWN ')
#     elif randomNum > userNum:
#         print('틀렸습니다. 다시 입력하세요.UP')
    
    
#     userNum = int(input('1~100의 숫자를 입력하세요. '))
#     count += 1
    
#     if count > 10:
#         print('게임에 졌습니다.')
#         break
# print(randomNum)

# quiz) 다음 요구조건을 참조하여 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램
'''
가로 길이는 1부터 2의 배수로 증가한다.
세로 길이는 1부터 3의 배수로 증가한다.
사각형의 넓이가 150보다 크면 프로그램을 종료한다.
가장 작은 사각형과 가장 큰 사각형의 넓이를 출력한다.
'''


width = 1
height = 1
minArea = width * height
maxArea = width * height

while True:

    area = width * height

    if area > 150:
        break

    print(f'가로: {width}, 세로: {height}, 넓이: {area}')
    
    
    if area < minArea:
        minArea = area

    if area > maxArea:
        maxArea = area

    if width == 1:
        width = 2
    else:
        width += 2

    if height == 1:
        height = 3
    else:
        height += 3

print(f'가장 작은 넓이: {minArea}')
print(f'가장 큰 넓이: {maxArea}')
    
    

        





