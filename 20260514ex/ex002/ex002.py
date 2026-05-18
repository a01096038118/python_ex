# flag = True

# members = {}

# while flag:
#    selectedMenuNum = int(input('1.회원가입:   2.프로그램 종료: '))

#    if selectedMenuNum == 1:
#       id = input('아이디 입력: ')
#       pw = input('비밀번호 입력: ')
#       members[id] = pw

#    elif selectedMenuNum == 2:
#       flag = False

#       for key in members:
#          print(f'ID: {key}, PW: {members[key]}')

# classes =  {
#    'python':'5학점', 
#    'C/C++':'5학점', 
#    'HTML5':'3학점', 
#    'Java':'5학점', 
#    'Javascript':'3학점'
#    }
# classes['HTML5'] ='5학점'
# classes['Javascript'] ='5학점'
# print(f'classes: {classes}')

# # ---------------------------------------

# for key in classes:
#     if classes[key] == '3학점':
#         classes[key] = '5학점'
# print(classes)


# members = {
#     '2019-052001': ['박찬호', 25, 'M', '010-1234-5678','헬스,수영',0],
#     '2019-052004': ['박용택', 65, 'M', '010-9012-2345','수영',50],
#     '2019-052003': ['박세리', 70, 'W', '010-7890-1234','아쿠아로빅',50]
# }

# # 전체 회원 정보 출력
# for key in members:
#     print(f'회원 번호: {key}, 회원 정보: {members[key]}')
# print('-' * 30)

# # 전체 회원 정보 출력 하는데, 회원의 '이름'과 '성별'만 출력을 하자.
# for key,value in members.items():
#     print(f'회원 번호: {key}, 회원 정보: {value[0]},{value[2]}')

# 딕셔너리 안에 딕셔너리
# members = {
#     '2019-052001': {
#         '이름':'박찬호',
#         '나이': 25, 
#         '성별': 'M', 
#         '연락처': '010-1234-5678',
#         '이용서비스': ['헬스', '수영'],  # -> 리스트타입
#         '할인율': 0
#         },
#          '2019-052004': {
#         '이름':'박용택',
#         '나이': 65, 
#         '성별': 'M', 
#         '연락처': '010-9012-2345',
#         '이용서비스': ['수영'],
#         '할인율': 50
#         },
#          '2019-052002': {
#         '이름':'박세리',
#         '나이': 70, 
#         '성별': 'W', 
#         '연락처': '010-7890-1234',
#         '이용서비스': ['아쿠아로빅'],
#         '할인율': 50
#         }
# }
# for key in members:
#     print(f'회원 번호: {key}, 회원 정보: {members[key]}')

# for key, value in members.items():
#     print(f'회원 번호: {key}, 회원 정보(이름, 성별): {value['이름']}, {value['성별']} ')

# for key, value in members.items():
#     print(f'회원 번호: {key}, 회원 정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')

# ---------------------------------------------------------------

vegetables = {
    '당근': 10,
    '건대추': 100,
    '대파': 20,
    '애호박': 3,
    '부추': 1
}
print(f'vegetables: {vegetables}')

vegetables['당근']-=1
vegetables['건대추']-=10
vegetables['대파']-=1
vegetables['애호박']-=1
vegetables['부추']-=1

for key,value in vegetables.items():
     print(f'vegetable: {key}, 재고량: {value[key]}')

# minvegetables = {
#     '당근': 1,
#     '건대추': 10,
#     '대파': 1,
#     '애호박': 1,
#     '부추': 1
# }
# for key,value in vegetables.items():
#      print(f'vegetable: {key}, 재고량: {value}')

