# 조건문(if문)
'''
if 조건식:
    실행문
'''

# num = 50
# if num > 10:
#     print('num은 10보다 크다.')
#     print('num은 10보다 크다.')

'''
if키워드 : 조건문을 선언하기 위한 키워드로 '만약 ~라면'의 뜻을 가지고 있다.
조건식 : 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정된다.
콜론 : 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.
실행문 : 조건식의 결과가 참(True)인 경우 실행하는 명령문이다.
        조건식의 결과가 거짓(False)이면 실행문은 실행되지 않는다.
'''

# 사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램을 만들어 봅시다.
# num = int(input('please input inteher numer)'))

# if num > 10:
#     print(f'{num}은 10보다 크다.')

# if num == 10:
#     print(f'{num}은 10보다 같다.')

# if num < 10:
#     print(f'{num}은 10보다 작다.')

# 속도위반 경고하기
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에게 경고를 하는 프로그램을 만들어봅시다.

# speed = int(input('자동차의 현재 속도 입력. '))
# if speed < 50:
#     print(f'정규속도 입니다')

# if speed == 50:
#     print(f'정규속도 입니다')


# if speed > 50:
#     print(f'속도위반 입니다')        

# if ~ else 구문
# else : 그렇지 않으면 이라는 뜻
# myScore = 70
# if myScore > 90:
#     print('용돈 획득')

# if myScore < 90:
#     print('몽둥이')    

# if myScore > 90:
#     print('용돈 획득')
# else:
#     print('몽둥이')    

# if ~ elif 구문        # 다중선택
'''
점수가 90이상이면 'A'출력
점수가 80 이상 90점 미만 'B'출력
점수가 70 이상 80점 미만 'C'출력
점수가 60 이상 70점 미만 'D'출력
'''
# myScore = int(input('점수 입력: '))
# if myScore >= 90:
#     print('A')
# elif (myScore >= 70) and (myScore < 80):        # 70이상 80미만
#     print('C')
# elif (myScore >= 80) and (myScore < 90):  
#     print('B')
# elif (myScore >= 60) and (myScore < 70):
#     print('D')
# else:
#     print('F')

# quiz) 자동 주문 시스템 만들기
'''
다국어를 지원하는 식당에서 사용할 자동 주문 시스템을 만들고자 한다.
1번을 누르면 한국어로, 2번을 누르면 영어로, 3번을 누르면 중국어로,
그 외 번호는 영어로 주문을 받는 프로그램을 만들어봅시다.

1.대한민국   2.USA    3.中国
1: 주문하시겠습니까?
2. Would you like to order?
3. 请问您要点餐吗？ 
그외 Would you like to order?
'''
#상수(CONST) : 한 번 데이터가 초기화 되면 영원히 바꿀수 없다.
# KOREA_NUMBER = 1               #상수
# USA_NUMBER = 2                 #상수
# CHINA_NUMBER = 3               #상수

# selectedNumber = int(input('1.대한민국   2.USA    3.中国'))
# if selectedNumber == KOREA_NUMBER:
#     print('주문하시겠습니까? ')
# elif selectedNumber == USA_NUMBER:
#     print('Would you like to order?')
# elif selectedNumber == CHINA_NUMBER:
#     print('请问您要点餐吗？?')    
# else:
#     print('Would you like to order?')

# quiz) 국가재난 지원금 수령액 조회하기
"""
다음은 가구 인원수에 따라 국가재난 지원금 수령액을 안내하는 프로그램이다.
표를 참고하여 프로그램을 만들어봅시다.
1인가구 : 400,000원
2인가구 : 600,000원
3인가구 : 800,000원
4인이상 가구 : 1,000,000원
"""
# onceFamily = 1
# twoFamily = 2
# thirdFamily = 3

# family = int(input('가구인원 수를 입력하세요.'))
# if family == onceFamily:
#     print('400,000원')
# elif family == twoFamily:
#     print('600,000원')
# elif family == thirdFamily:
#     print('800,000원')
# else:
#     print('1,000,000원')

'''
다음 요구사항을 충족하는 프로그램을 if ~ elif문을 이용해서 만드세요.
BMI 지수를 입력한다.
BMI 지수가 90 이하면 '저체중'을 출력한다.
BMI 지수가 90 초과 110 이하면 '정상 체중'을 출력한다
BMI 지수가 110 초과 120 이하면 '과체중'을 출력한다
BMI 지수가 120 초과 140 이하면 '비만'을 출력한다
BMI 지수가 140 초과면 '고도 비만'을 출력한다
'''

# bmiWeight = int(input('체중을 입력하세요: '))
# if bmiWeight <= 90:
#     print('저체중')
# elif (bmiWeight >= 90) and (bmiWeight < 110):
#     print('정상 체중')
# elif (bmiWeight >= 110) and (bmiWeight < 120):
#     print('과체중')
# elif (bmiWeight >= 120) and (bmiWeight < 140):
#     print('비만')
# else:
#     print('고도 비만')

# 중첩 조건문
# 조건문 내에 또 다른 조건문을 쓸 수 있는데 이를 종첩 조건문이라고 합니다.
# 사용자가 입력한 정수에서 양수(0도 포함)인지를 판단하고 양수라면 홀/짝인지 구분하자.

# myInteger = int(input('정수 입력: '))
# if myInteger > 0:
#     print('양수')
#     if myInteger % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('음수')

# 짝수/홀수를 판별하는 프로그램을 만들자
# num = int(input('사용자야 양의 정수 입력해줘라'))
# if num > 0:
#     if num % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('입력한 정수는 0 또는 음수입니다.')

# '''
#  출생연도 끝자리(endBirthYear)와 나이(age)를 입력하면 다음 요구사항에 맞춰 
# 마스크 구매 가능한 요일을 출력하는 프로그램을 만들어보자.

# - 공적 마스크 판매 관련해서 출생연도 끝자리를 이용한 5부제를 다음과 같이 실시한다.
# -1,6 => 월
# -2,7 => 화
# -3,8 => 수
# -4,9 => 목
# -5,0 => 금
# -만 65세 이상 어르신은 언제든지 구매 가능하다.
# '''
# endBirthYear = int(input('출생연도 끝자리 입력: '))
# age = int(input('나이 끝자리 입력: '))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear == 6:
#         print('월요일에 구매 가능합니다.')
#     elif endBirthYear == 2 or endBirthYear == 7:
#         print('화요일에 구매 가능합니다.')
#     elif endBirthYear == 3 or endBirthYear == 8:
#         print('수요일에 구매 가능합니다.')
#     elif endBirthYear == 4 or endBirthYear == 9:
#         print('목요일에 구매 가능합니다.')
#     elif endBirthYear == 5 or endBirthYear == 0:
#         print('금요일에 구매 가능합니다.')
# else:
#     print('언제나 구매 가능합니다.')


# 날짜 관련 모듈 : datetime
# from datetime import datetime
# # 현재 일 구하기
# print(datetime.today().weekday())
# """
# 고농도 미세먼지 비상저감조치를 위한 2부제 프로그램입니다.
# 다음 요구사항 결과 화면을 참고하여 프로그램을 완성해봅시다
# 오늘 날짜를 구한다
# 차량번호 4자리를 입력한다
# 2부제에 따라 오늘 날짜와 차량번호를 비교해서 입차 가능 여부를 출력한다.
# """

# """
# 고농도 미세먼지 비상저감조치를 위한 2부제 프로그램입니다.
# 다음 요구사항 결과 화면을 참고하여 프로그램을 완성해봅시다
# 오늘 날짜를 구한다
# 차량번호 4자리를 입력한다
# 2부제에 따라 오늘 날짜와 차량번호를 비교해서 입차 가능 여부를 출력한다.
     
# """
      
# from datetime import datetime

# dayNum = datetime.today().day
# carNum = int(input('차량번호 4자리 입력하세요.'))

# print(f'오늘날짜: {dayNum}일')
      
# if dayNum % 2 ==0:
#     print('오늘 입차: 번호가 짝수인 차량')
# else:
#     print('오늘 입차: 번호가 홀수인 차량')

# if dayNum % 2 ==carNum % 2:
#     print('귀하의 차량은 입차 가능합니다.')
# else:
#      print('귀하의 차량은 불가 가능합니다.')

# '''
# 다음 표는 심장 정지 환자에게 자동 심장 충격기를 사용했을때 최초로 시행한 시간데 따른
# 환자의 생존율을 나타냅니다.
# 장비를 사용하기까지 걸린 시간을 입력하면 생존율이 출력되는 프로그램을 만들어봅시다.
# '''
# time = int(input('최초 장비사용 걸린 시간: '))
# if time <= 60:
#     print('생존율: 85%')
# elif time <= 120:
#     print('생존율: 76%')
# elif time <= 180:
#     print('생존율: 66%')
# elif time <= 240:
#     print('생존율: 57%')
# elif time <= 300:
#     print('생존율: 47%')
# else:
#     print('생존율 25% 미만')

# 누진세가 적용된 단가표를 참고하여 전기 사용량을 입력하면
# 전기료가 출력되는 프로그램을 만들어봅시다.


# price = 0
# basic = 0
# kwh = int(input('전기사용량: '))

# if kwh <= 200:
#     price = 99.3
#     basic = 910

# total = ({kwh *price * basic})
# print('total')

# 어린이의 신장을 입력하면 놀이기구 탑승 여부가 출력되는 프로그램을 만드시오
# 놀이기구 탑승은 신장이 최소 120cm부터 최대 160cm까지 가능하다
# height = int(input('신장 입력: '))
# if height >= 120 and height <= 160:
#     print('탑승가능')
# else:
#     print('탑승 불가능')

# testScore = int(input('시험점수를 입력하세요, '))
# if testScore >= 85:
#     print('success')
# else:
#     print('fail')

# testScore = int(input('시험점수를 입력하세요, '))
# result = 'success' if 85 <= testScore else 'fail'
# print(f'result: {result}')

# import random        # 난수 발생 모드

# randNum = random, randint(1, 3)       # 1부터 3까지의 정수중에서 하나는 발생한다.

# myNum = int(input('1.가위 2.바위 3.보 를 선택하세요. '))

# if randNum == myNum:
#     print('무승부')

# elif (randNum == 1 and myNum == 2) or \
#     (randNum == 2 and myNum == 3) or \
#         (randNum == 3 and myNum == 1):
#     print('사용자 승')

# elif (randNum == 1 and myNum == 3) or \
#     (randNum == 2 and myNum == 1) or\
#           (randNum == 3 and myNum == 2):
#     print('컴퓨터 승')

# '''
# 사용자가 입력한 문자 메세지 길이에 따라서 SMS 또는 MMS의 발송을 결정하는 프로그램을 완성하자
# (단, 메세지 길이가 50 이하면 SMS 발송, 그렇지 않으면 MMS를 발송한다.)
# '''

# str = 'hello'
# print(f'str: {str}')
# print(f'str\' lenght: {len(str)}')

# useMessage = input('메세지를 입력하세요: ')
# msgLen = len(useMessage)

# if msgLen <=50:
#     print('SMS 발송')
# else:
#     print('MMS 발송')