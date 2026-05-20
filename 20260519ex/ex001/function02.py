# 지역변수 vs 전역변수
# 지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능하다.
# 전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용가능하다.

# num = 10

# def fun():
#     # num = 20             # 지역변수
#     global num
#     num = num + 1          # 데이터 수정 num(전역변수) = 10 + 1
#     print(f'num: {num}')   # 10, 전역변수 num -> 20, 지역변수 num
    

# print(f'num: {num}')       # 10, 전역변수 num

# fun()

'''
global 키워드는 함수 내에서 전역변수의 값을 수정하고자 할때 반드시 명시하자.
'''

# quiz) 웹사이트읜 누적 방문 횟수 프로그램
# 웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다.

# flag = True
# totalVisitor = 0

# def countVisitor():
#     global totalVisitor
#     totalVisitor += 1

# while flag:
#    selectedMenuNum = int(input('1. 웹사이트 방문    2. 종료'))

#    if selectedMenuNum == 1:
#        countVisitor()
#        print(f'누적 방문 횟수: {totalVisitor}')

#    else:
#        flag = False
#        print('종료 ')

# ***************** 매개변수 *******************
# 매개 : 둘 사이에서 양편의 '관계를 맺어' 줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 출력할때 호출.
# 이 때, 함수를 정의하는 쪽을 함수정의부(선언부), 함수를 호출 하는 쪽을  호출부라고 한다.
# 함수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고 한다.
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장한다. 그리고 매개변수는 지역변수의 일종이다.

# def greet(name, age):
#     # name = '홍길동' or '박세리' or '박찬호'
#     print(f'{name} 안녕하세요. 나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박세리', 20)
# greet('박찬호', 30)

# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다.')
#     print(f'최고 온도: {temp}도')
#     print(f'평균 습도: {humi}%')
#     print(f'비올 확율: {rain}%')

# forecastWeather(32, 67, 50)

# 인수의 개수를 모르는 경우
# 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자.
# 우리 학급 학생 수는 총 3명이다.


# def printScoresForStudent(score1, score2, score3):
#     totalScore = score1 + score2 + score3
#     averageScore = totalScore / 3

#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

# def printScoresForStudent(subject, *scores):        # 리스트(list) -> 튜플(tuple)

#     print(f'scores type: {type(scores)}')  # tuple
#     print(f'scores length: {len(scores)}') # 3
    
#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     print(f'{subject}총합: {totalScore}')
#     averageScore = totalScore / len(scores)
#     print(f'{subject}평균: {averageScore}')


# printScoresForStudent('국어', 96, 87, 98, 95, 53)

# '''
# 선생님이 몇명일지 모르는 학생의 점수를 입력한다.
# 이때 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들자.
# '''
# flag = True
# studentScores = []

# def printScoresForStudent(scores):       # scores = [,,,,,,,,,,]
#     totalScore = 0
#     for score in scores:
#       totalScore += score
      
#     average = totalScore / len(scores)
#     print(f'총점: {totalScore}')
#     print(f'평점: {average}')

# while flag:
#     selectedMenuNum = int(input('1. 학생점수 입력     2. 종료 '))
#     if selectedMenuNum == 1:  
#         score = int(input('학생점수 입력: '))
#         studentScores.append(score)
#     else:
#         flag = False

# printScoresForStudent(studentScores)



# SNS 와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다. 
'''

# def sendUserMessage(str):
#     strLength = len(str)
#     print(f'사용자가 입력한 문자 길이: {strLength}')

#     if strLength <=100:
#         print(f'SMS 발송 완료')
#         print('50원 부과')
#     else:
#         print(f'MMS 발송')
#         print('100원 부과')

# inputData = input('문자입력: ')
# sendUserMessage(inputData)

# 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):
#     print(f'Name\t: {name}')
#     print(f'Email\t: {email}')
#     print(f'Major\t: {major}')
#     print(f'Grade\t: {grade}')
#     print('---------------------------------')

# printMemberInfo(email = 'gildong@gmail.com', 
#                 name = 'Hong Gildong', 
#                 major = 'are', 
#                 grade = 1)

# def printMemberInfo(info):
#     print(f'email: {info['email']}')
#     print(f'major: {info['major']}')
#     print(f'grad: {info['grade']}')
#     print(f'name: {info['name']}')
    

# printMemberInfo({
#         'major': 'art',
#         'grade': 1,
#          'name': 'Hong gildong',
#         'email': 'gildong@gamail.com',
#     })

# # 매개변수의 기본값 설정
# # 직원 급여 지급 프로그램을 만들어보자
# def setSalary(name, pay = 200):
#     print(f'{name}의 급여는 {pay}만원 지급')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택')

# 데이터 반환(return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
# 이때 사용하는 키워드가 return 입니다.
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자.

# def printResult(value):
#     print(f'result: {value}')
# def addFuntion(n1, n2):
#     sum = n1 + n2                # 30
#     # print(f'결과값: {sum}')
#     printResult(sum)
#     return sum

# addFuntion(10, 20)               # 호출
# print(f'result : {result}')

# DEV_MOD = False

# def fun1():
#     print('1111111111111')
#     if DEV_MOD == True:
#         print('2222222222222')        # 개발 단계에서 디버깅 용도로만 사용한다.
#         return
#     print('3333333333333')

# fun1()

# 별탑 만들기
# def increaseStar(limitStarCount):
#     # print('*')
#     # print('**')
#     # return
#     # print('***')
#     # print('****')
#     # print('*****')
#     # print('******')
#     # print('*******')
#     for n in range(1,8):
#         print('*' * n)
#         if n == limitStarCount:
#             break
# increaseStar(5)

# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴는 1.  회원가입 2.  로그인  3. 특정회원 정보 출력  4. 모든 회원 정보출력     99.  종료
사용자가 1. 회원가입을 선택하면 회원ID, 회원PW, 회원Email, 회원 연락처 정보를 입력받아 회원가입 진행한다.
2. 로그인을 선택하면  회원ID, 회원PW를 입력받아 로그인 '성공', 또는 '실패'를 출력한다.
3. 특정 회원 정보를 출력을 선택하면 회원ID와 회원PW 를 입력받아 일치하는 회원 정보를 출력한다.
4. 모든 회원 정보 출력을선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99. 종료 를 선택하면 프로그램 종료시킨다.

특정회원의 회원ID와 회원pw를 입력받아 인증되면 회원정보를 수정하는 기능을 구현해 보자.
'''

flag = True
myProfile = {}

while flag:
    selectNum = int(input('1.회원가입  2.로그인  3.특정회원 정보 출력  4.모든 회원 정보 출력  99.종료 '))
    if selectNum == 1:
        selectId = input('회원 ID: ')
        selectPw = input('회원 PW: ')
        selectEmail = input('회원 EMAIL: ')
        selectPhoneNum = input('회원 연락처: ')

        myProfile[selectId] = {
            'uId': selectId,
            'uPw': selectPw,
            'uEmail': selectEmail,
            'uPhone': selectPhoneNum,
        }

        print(f'myProfile: {myProfile}')

        # myProfile.append(profile)
        print('회원가입 성공')

    elif selectNum == 2:
         selectId = input('회원 ID: ')
         selectPw = input('회원 PW: ')
         selectEmail = input('회원 EMAIL: ')
         selectPhoneNum = input('회원 연락처: ')
         if selectId in myProfile:

            if myProfile[selectId]['uPw'] == selectPw:
                print('로그인 성공')
            else:
                print('로그인 실패')


    elif selectNum == 3:
         
         selectId = input('회원 ID: ')
         selectPw = input('회원 PW: ')

         if selectId in myProfile:
             if myProfile[selectId]['uPw'] == selectPw:
                 print(f'myProfile: {myProfile}')

       

    elif selectNum == 4:
        print(f'myProfile: {myProfile}')
    else:
        newEmail = myProfile['uEmail'] = 'gildong@gmail.com'
        print(f'newEmail: {newEmail}')
