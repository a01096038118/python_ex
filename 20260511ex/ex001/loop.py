# 반복문(for문 & while문)

# for문 : ~ 하는 동안 -> 횟수에 의한 반복
'''
for 변수 in 범위: 
    실행구문
'''
# 1~10까지의 정수를 출력
# 1~n까지의 정수 range (1, (n+1), 1)
# for num in range(1, 11, 1):
#     print(f'{num}: hello')

# 0부터 10까지의 정수를 출력
# for num in range(0, 11, 1):       # -> 총 11회 반복
#     print(f'num ={num}')

# range() 간략화
# for num in range(11):     # == range(0, 11,1)   # 단계가 1인 경우 단계를 생략할 수 있다.
#     print(f'num ={num}')       # 단계가 생략되고 시작이 0이면 시작도 생략 가능하다.

# 2~ 8 사이의 짝수 출력
# for num in range(2,9,2):
#     print(f'num ={num}')

# for num in range(1,16):
#     if (num <= 8) and (num %2==0):
#         print(f'num = {num}')

# quiz)
# 사용자가 입력한 횟수만큼 '메일발송!' 문자열 출력하기
# for measege in range(7):
#     print(f'measege: {'메일발송!'}')

# measege = int(input('숫자를 입력해주세요: '))
# for measege in range(measege):
#     print('메일발송!')

# quiz)
# 1~10 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기
# for num3 in range(1,11,1):
#     if num3 %3== 0:
#         print('3의배수!')
#     else:
#         print(num3)

# for i in range(1, 11):
#     print('3의 배수!' if (i % 3 == 0) else i)

# 사용자 원하는 구구단을 입력하면 해당 구구단을 출력하자
# userInputData = int(input('숫자를 입력하세요: '))
# for matMat in range(1,10):
#     print(f'{userInputData}*{matMat} = {userInputData*matMat}')
# userInputData = int(input('숫자를 입력하세요: '))
# for matMat in range(1,10):
#     resultStr = f'{userInputData}*{matMat} = {userInputData*matMat}'
#     print(resultStr)



#1~10까지 정수의 합 출력하기
# userInput = int(input('정수입력: '))
# sum = 0
# for i in range(1, userInput +1 ):
#     sum += i
# print(f'1부터 {userInput}까지의 합: {sum}')

#for문을 이용해서 1~100까지의 정수중에서
#3과 7의 공배수와 최소공배수를 출력하시오.

# minNum = 0            21
# for num in range(1, 101):
#     if num % 3 == 0 and num % 7 == 0:      # 3의 배수 and 7의 배수 21 42
#         print(f'3과 7의 공배수: {num}') 
#         if minNum == 0: minNum = num

# print(f'3과7의 최소공배수: {minNum}')


# for ch in 'Hello':         # ch :캐릭터 약자
#     print(f'ch: {ch}')

#50 보다 작은 7의 배수를 출력하는 프로그램을 만들어보자
# for num in range(1,51):
#     if num % 7 ==0:
#         print(f'num: {num}')

# while문 : ~ 하는동안 -> 조건에 의한 반복 

# num = 1
# while num <= 10:
#     print(f'num: {num}')
#     num += 1

# quiz) 1부터 30까지 정수 중 홀수와 짝수 구분하여 출력하기

# num = 1              # 시작값
# while num < 31:      #조건(끝)
#     num += 1         #단계
#     if num % 2 == 0:
#         print(f'{num}은 짝수')
#     else:
#         print(f'{num}은 홀수')

# quiz 구구단 3단 출력하기 by while문

# userInputData = int(input('숫자를 입력하세요: '))
# num = 1
# while num < 10:
#     num += 1
#     print(f'{userInputData}*{num} = {userInputData * num}')


 # quiz) 구구단 2단부터 9단 전체 만들어보기
# num1 = 1
# while  num1 < 10:
#     num2 = 2
#     str = ''     # '' -> 초기화
#     while num1 < 10:
#         str += f'{num2} x {num1} = {num2 * num1}\t' 
#         # 2 x 2 = 2(#문자열의 결과값을 나타내기위해 str사용) 
    
#     print(str)
#     num1 += 1

# quiz) while문과 if문을 이용해서 0~100까지 정수 중 3과 8의 공배수와 최소 공배수 출력하기

# myNum = 1       # 반복문의 시작
# num = 0         # 최소공배수
# while myNum <= 100:
    
#     if myNum % 3 == 0 and myNum % 8 == 0:
#         print(f'3과 8의 공배수: {myNum}') 
#     myNum += 1
#     if num == 0:
#        num = myNum

# print(f'3과 8의 최소 공배수: {num}')

# 반복문 내 실행 제어 : break, continue
#continue : 키워드를 사용하면 이후 반복실행을 생략하고 다시 반복문의 처음으로 돌아간다.
# continue를 이용해서 1부터 10까지의 정수 중 홀수만 출력하는 프로그램을 만들어보자.
# for num in range(1,11):
#     if num % 2 ==0:
#         continue
#     print(f'num: {num}')


# count = 1
# for num in range(10):
#     print(f'num: {num}')
#     count += 1
#     if count >=5:
#         break

# break : 
# 반복문에서 break를 만나면 '실행을 즉시 중단하고 반복문을 빠져나온다.
# 1부터 10까지의 정수를 더하되, 결과가 30 이상이 될때 정수를 찾는 프로그램을 만들어보자.

# num = 1
# sum = 0
# while num < 11:
#     sum += num
#     if sum >= 30:
#         print(f'num: {num}')
#         break
#     num += 1
# print(f'sum: {sum}')

# for ~ else 
# """
# for문에서 else 키워드를 사용하는 경우, else 이하의 구문은 for문의 반복 업무를
# 모두 완료하고 난 후 실행됩니다.
# """

# # 1부터 5까지 정수를 입력하고 반복문이 끝나면 완료 메세지를 출력하자.
# for num in range(1,6):
#     print(f'num: {num}')
# else:
#     print('완료')

# quiz)
# '''
# 삼각형 넓이 구하기
# 가로와 세로의 길이를 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어보자.
# 단, 가로길이는 1부터 2의 배수로 증가하고
# 세로길이는 1부터 3의 배수로 증가하여
# 삼각형의 넓이가 150보다 크면 프로그램을 종료한다.
# '''
# count = 1
# maxArea = 150

# while True:
#     result = ((count * 2) * (count * 3)) /2
#     if result > 150:
#         break

#     print(f'삼각형의 넓이: {result}')
#     count += 1
    
