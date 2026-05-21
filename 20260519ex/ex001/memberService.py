# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입  2.로그인   3.나의 회원 정보 출력  4.모든 회원 정보 출력  5. 회원 탈퇴 6. 회원정보 수정 99.종료
사용자가
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선책하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.나의 회원 정보 출력'를 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.

심심하면> 나의 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해 보자!

'''
SING_UP               = 1
SING_IN               = 2
PRINT_MY_INFO         = 3
PRINT_ALL_MEMBER_INFO = 4
SYSTEM_SHUTDOWN       = 99

DEV_MOD = True

members = {}

if DEV_MOD:   
    
    uIds = ['gildong', 'chanho', 'sarei' ]
    uPws = ['1234', '5678', '9012' ]
    uMails= ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net' ]
    uPhones = ['010-1234-5678', '010-9999-8888', '010-7777-6666' ]

    for n in range(len(uIds)):      # 3회 반복 ( 0, 1, 2 )
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
            }

# functions START

def getSelctedMenuNum():
    selectedMenuNum = int(input('1.회원가입  2.로그인   3.나의 정보 출력   4.모든 회원 정보 출력   5. id/pw 찾기 6. 회원탈퇴 99.종료'))
    return selectedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):     
        members[uIds] = {
            'uId' : uId,
            'uPw' : uPw,
            'uMail' : uMail,
            'uPhone' : uPhone
            }

def isMember(uId):
     if uId in members:
        print(f'{uId}는 이미 사용중 입니다. 다시 확인하세요')
        return True
     else:
         return False
     
def printAllMemberInfo(value):
      for key1, value1 in value.items():
                print(f'{key1}: {value1}')

# functitios = END

flag = True

while flag:
    
    userSelectedMenuNum = getSelctedMenuNum()
    
    if userSelectedMenuNum == SING_UP:
        uId = input('Input member ID: ') 
        if not isMember(uId):
            uPw = input('Input member PW: ') 
            uMail = input('Input member EMAIL: ') 
            while True:
                if '@' not in uMail:
                    print('입력한 이메일 주소가 형식에 맞지않습니다.')
                    uMail = input('Input member EMAIL: ')
                else:
                    break

            uPhone = input('Input member PHONE: ')

            setNewMember(uId, uPw, uMail, uPhone)

            print('SIGN-UP SUCCESS')
                
            if DEV_MOD : print(f'members: {members}')

    elif userSelectedMenuNum == SING_IN:                    # 2. 로그인
        signInCnt = 1
        while True:
            uId = input('Input member ID: ') 
            uPw = input('Input member PW: ') 
            
            if uId in members:
                uInfo = members[uId]
                if uInfo ['uPw'] == uPw:
                    print('SIGN-IN SUCCESS')
                else:
                    print('SIGN-IN FAIL')
                    signInCnt += 1
                    if signInCnt > 3:
                        print('3회 이상 틀렸어요. ')
                        break
            else:
                print('존재하지 않는 ID입니다. 다시 확인하세요. ')

    elif userSelectedMenuNum == PRINT_MY_INFO :             # 3. 나의 정보 출력
        uId = input('Input member ID: ') 
        uPw = input('Input member PW: ') 
        
        if uId in members:
            uInfo = members[uId]
            if uInfo ['uPw'] == uPw:
                print('SIGN-IN SUCCESS')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)
             
            else:
                print('SIGN-IN FAIL')
            
        else:
            print('존재하지 않는 ID입니다. 다시 확인하세요. ')

    elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:      # 4. 모든 회원 정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보 ------------- ')
            printAllMemberInfo(value)
            print('-' * 30)


    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:            # 99. 종료
        flag = False
        print('The End')