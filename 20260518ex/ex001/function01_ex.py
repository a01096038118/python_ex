# goods = {
#     '새우깡': 1200,
#     '비비빅': 400,
#     '초코파이': 500,
#     '맛동산': 1500
# }

# totalPrice = 0

# def shrimpCrackerPrice():
#     global totalPrice
#     totalPrice += goods['새우깡'] * shrimpCrackers
#     print(f'새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}원')

# def bibibigPrice():
#     global totalPrice
#     totalPrice += goods['비비빅'] * bibibigs
#     print(f'비비빅 구매 금액: {goods['비비빅'] * bibibigs}원')

# def chocopiPrice():
#      global totalPrice
#      totalPrice += goods['초코파이'] * chocopies
#      print(f'초코파이 구매 금액: {goods['초코파이'] * chocopies}원')

# def matdongsanPrice():
#     global totalPrice
#     totalPrice += goods['맛동산'] * matdongsans
#     print(f'맛동산 구매 금액: {goods['맛동산'] * matdongsans}원')

# shrimpCrackers = int(input('새우깡 구매개수: '))
# bibibigs = int(input('비비빅 구매개수: '))
# chocopies = int(input('초코파이 구매개수: '))
# matdongsans = int(input('맛동산 구매개수: '))


# print(f'새우깡 구매개수 : {shrimpCrackers}')
# print(f'비비빅 구매개수 : {bibibigs}')
# print(f'초코파이 구매개수 : {chocopies}')
# print(f'맛동산 구매개수 : {matdongsans}')
# print('=' * 40)

# shrimpCrackerPrice()
# bibibigPrice()
# chocopiPrice()
# matdongsanPrice()
# print('=' * 40)
# print(f'총 구매 금액: {totalPrice}')
# print('=' * 40)

# count = 0
# def increase():
#     global count
#     count = count +1
#     print(count)

# increase()

# age = 25
# print(f'age: {age}')


# student = {                    # student 라는 변수값 안에 데이터를 갖고있다.
#     '이름': '홍길동',
#     '나이': 25
# }

# print(f'나이: {student['나이']}')

# def modifyStudentAge():
#     student['나이'] += 1
# modifyStudentAge()

student01 = {            # 얕은 복사
    '이름': '홍길동',
    '나이': 25
}

student02 = student01
student01['나이'] = 100
print(student02['나이'])

import copy              # 깊은 복사
student01 = {
    '이름': '홍길동',
    '나이': 25
}
student02 = copy.deepcopy(student01)

student01['나이'] = 1000
print(student02['나이'])