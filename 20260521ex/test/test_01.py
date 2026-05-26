SIGN_UP = 1
SIGN_IN = 2
MEMBER_MODIFY = 3
MEMBER_READ = 4
SIGN_OUT = 5
SYSTEM_OUT = 99



members ={}

def usersignInedMemberId():
    signInedMemberId = int(input('1.sign-up   2.sign-in  3.modify  4.read  5.sign-out  99.end '))
    return signInedMemberId

def userPwNumber():
    if uPw in members[uId]['uPw'] == uPw:
        print(f'회원정보: {members}')
    return signInedMemberId

def notIdnNumber():
    print('입력하신 ID가 아닙니다.')
    print('다시 입력해주세요.')
    return SIGN_IN


flag = True
while flag:
  
    signInedMemberId = usersignInedMemberId()   
    
    if signInedMemberId == SIGN_UP:
        uId = input('ID: ')
        while True:
            uPw = input('PW: ')
            if '@' not in uPw and '!' not in uPw:
                print('사용할 수 없는 PW입니다')
                print('다시 입력해주세요. ')
            else: 
                break
        while True:
            uMail = input('MAIL: ')
            if '@' in uMail and '.' in uMail:
                break 
            else:
                print('올바른 EMAIL형식이 아닙니다. ')
                print('다시 입력해주세요. ')

        while True:
            uPhone = input('PHONE: ')
            if '-' not in uPhone:
                print('잘못입력하셨습니다. ')
                print('다시 입력해주세요. ')
            else:
                break 

        members[uId]= {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
            }

        print(members)
        print('suceess sign-up ')

    if signInedMemberId == SIGN_IN:
        while True:
            uId = input('ID: ')
            if uId in members:
                print('올바른 ID입니다.')
                break
            else:
                notIdnNumber()

        while True:
            uPw = input('PW: ')
            if uPw in members[uId]['uPw'] == uPw:
                print('success ssign-in')
                break
            else:
                print('입력하신 PW가 아닙니다.')
                print('다시 입력해주세요.')
    if signInedMemberId == MEMBER_MODIFY:
        uPw = input('PW: ')
        if members[uId]['uPw'] == uPw:
            newPW = input('newPw: ')
            members[uId]['uPw'] = newPW
            print(f'newPW: {newPW}')
            print('PW 수정 완료. ')
        else:
            print('잘못된 비밀번호입니다.')

    if signInedMemberId == MEMBER_READ:
        while True:
            uPw = input('PW: ')
            if userPwNumber():
                break

            else:
                print('입력하신 PW가 아닙니다.')
                print('다시 입력해주세요.')
    
    if signInedMemberId == SIGN_OUT:
        uPw = input('PW: ')
        del members[uId]
        print('sign-out')
           
    if signInedMemberId == SYSTEM_OUT:
           print('종료합니다. ')
           flag = False