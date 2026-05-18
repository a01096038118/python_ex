# 딕셔너리 정의
# 딕셔너리는 {} 를 이용한다.

# ages = {'박찬호': 48, '박지성': 40, '박세리': 50, "이승엽": 43, '박찌성': 40}
# print(f'ages: {ages}') 
# print(f'ages type: {type(ages)}') 

# scores = {'c/c++': 'A', 'Java': 'B+', '네트워킹': 'C', 
#  '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
# print(f'scores: {scores}')

# 마지막 내용: **********************************************************
# 리스트, 튜플, 딕셔너리

# listVar = [3, 3.14, ' hello']
# print(f'listVar: {listVar}')

# tupleVar = [3, 3.14, ' hello']
# print(f'tupleVar: {tupleVar}')


# dictVar = {'홍길동': 10, 
#            '박찬호': '열살', 
#            '박세리': 3.14,}

# listVar1 = [1, 2, 3]
# listVar2 = [1, 2, 3, listVar1]

# print(f'listVar1: {listVar1}')       # [1, 2, 3]
# print(f'listVar2: {listVar2}')       # [1, 2, 3, [1, 2, 3]]

# listVar2[3]
# print(listVar2[3][1])                # 2

# print(type(listVar2[3]))             # list
# print(type(listVar2[3][1]))          # int

# dicts = {
#     'name': '박찬호' ,
#     'age': 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구']
# }

# print(f'dicts: {dicts}')
# # dicts: {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 'hobby': ['축구', '농구', '배구']}

# dicts['hobby'] [1]   # ['축구', '농구', '배구']

# print(dicts['hobby'][1])      # 농구

'''
딕셔너리 조회/ 삽입/ 수정/ 삭제
CRUD: 컴퓨터 프로그램에서 '조회/ 삽입/ 수정/ 삭제
CRUD는 Create, Read, Update, Delete를 말합니다.
즉 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 하는것을 말한다.
그렇다면, 딕셔너리에서 CRUD는 딕셔너리 컨테이너 자료형에
데이터를 추가(Create), 조회(Read), 수정(Update), 삭제(Delete) 하는것을 말한다.
CRUD는 프로그래밍 뿐만 아니라 데이터베이스에서도 사용되는 용어이다. 
'''

# 추가(Create)
dicContainer = {
    '이름': '홍길동',
    '나이': 25,
    '주소': '대전 중구',
    '취미': ['축구', '수영', '조깅'],
    '몸무게': 87.5
}
print(f'dicContainer: {dicContainer}')

dicContainer['연락처'] = '010-1234-5678'
print(f'dicContainer: {dicContainer}')

# 조회(Read)
dicContainer['이름']
print(f'이름: {dicContainer['이름']}')

# 수정(Update)
dicContainer['몸무게'] = 50
print(f'몸무게: {dicContainer['몸무게']}')

# 삭제(Delete)
del dicContainer['몸무게']
print(f'dicContainer: {dicContainer}')

# 부가 기능들
# 아이템 개수 조회
print(f'아이템개수: {len(dicContainer)}')

# 전체 키 & 벨류를 조회
# 전체 키 
dicKeys = dicContainer.keys()
print(f'dicKeys: {dicKeys}')            # 결과값이 리스트로 변환해서 나옴

for key in dicKeys:
    print(f'{key} : {dicContainer[key]}')   # 전체 아이템 나옴

# 전체 벨류값 구하기
dicValues = dicContainer.values()
print(f'dicValues: {dicValues}')

# 키와 벨류를 한방에 조회
for key , value in dicContainer.items():
    print(f'{key}: {value}')

    # 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''
 # -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
 #   딕셔너리를 만든다.
scores = {
    'C/C++': 'A',
    'Java': 'B+',
    '모바일': 'C',
    '보안': 'A+',
    '해킹': 'F',
    '시스템': 'C+'
}
#-2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
print(f'Jave: {scores['Java']}')
print(f'시스템: {scores['시스템']}')

# -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(f'scores: {scores}')

# -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores: {scores}')

# -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다. (합, 평균 추가)

# ------------------------------------------------------
creditScores = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C': 2.5,
    'C': 2.0,
    'F': 0.0
    }
totalScore = 0
averageScore = 0

for key in scores.keys():
    totalScore += creditScores[scores[key]]
    print(f'{key}:\t{scores[key]}')

print(f'totalScore: {totalScore}')
averageScore = totalScore/ len(scores)
print(f'averageScore: {averageScore}')
'''
C/C++:  A
Java:   F
모바일: C
보안:   A+
해킹:   F
시스템: A
파이썬: A
OS:     A+
'''
# ------------------------------------------------------
'''
A+  : 4.5
A   : 4.0
B+  : 3.5
B   : 3.0
C   : 2.5
F   : .0
'''
