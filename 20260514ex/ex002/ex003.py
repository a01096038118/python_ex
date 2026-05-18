# CRUD
'''
C : Creat     생성, 추가
R : Read      조회
U : Update    수정
D : Delete    삭제
'''

'''
딕셔너리(Dictionart): {key: value}
'''
student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'
}

print(f'studnet: {student}')
print(f'studnet type: {type(student)}')

# R: Raed
sNo = student['학번']
print(f'sNo: {sNo}')
print(f'sNo type: {type(sNo)}')

# U: Update
sName = student['이름']
print(f'sName: {sName}')

sName = student['이름'] = '홍길자'
print(f'sName: {sName}')
print(f'sName type: {type(sName)}')

# D :Delete
del student['연락처']
print(f'student: {student}')

# keys(), values(), items()
#keys() : 딕셔너리 자료형에서 키값들만 뽑는다. 뽑은 keys는 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')

for key in keys:
    print(f'key: value = {key} : {student[key]}')

# values() : 딕셔너리에서 value값들만 뽑는다.뽑은 value들은 리스트와 비슷한 데이터 타입이다.
values = student.values()
print(f'values: {values}')
print(f'values type: {type(values)}')

for value in values:
    print(f'value: {value}')

items = student.items()
print(f'items: {items}')   # ([('학번', 123456789), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])
print(f'items type: {type(items)}') # dict_items type

for item in items:
    print(f'item: {item}')
    print(f'item[0], item[1]: {item[0]},{item[1]}')

'''
item 튜플 ('학번', 123456789) == item[0], item[1]
'''

'''
key , value = ('학번', 123456789)
'''

for key, value in items:   # 구조분해할당 문법
    print(f'key, value = {key}, {value}')

# 구조 분해 할당
a, b = ( 10, 20 )
print(f'a: {a}, b: {b}')

a = 10
b = 20

# swapping ==> a: 20 b, :10
a, b = b, a
print(f' a: {a}, b: {b}')

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = [30, 40, 50, 60]
'''

a, b, *c = scores
print(f' a: {a}, b: {b}, c: {c}')   #  a: 10, b: 20, c: [30, 40, 50, 60]

# quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
# 표를 보고 파이썬을 이용해서 컨테이너 자료형으로 만드시오.

members = {
    '2019-052001' : {
        '이름': '박찬호', 
        '나이': 25, 
        '성별': 'M', 
        '연락처': '010-1234-5678', 
        '이용서비스': ['헬스,수영'], 
        '할인율': 0 }
}
# info = members['2019-052001']
# print(f'info: {info}')

# infos = info.split('+')
# print(f'infos: {infos}')

print(members ['2019-052001'])
members['2019-052001']['이름']
members['2019-052001']['나이']
members['2019-052001']['할인율']
members['2019-052001']['이용서비스']
print(members ['2019-052001'] ['이름'])
print(members ['2019-052001'] ['나이'])
print(members ['2019-052001'] ['할인율'])
print(members ['2019-052001'] ['이용서비스'])