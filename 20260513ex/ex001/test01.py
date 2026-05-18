# # quiz) 회의 참석자 정렬하기
# #다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# names.sort()
# print(f'names: {names}')
# names.sort(reverse = True)
# print(f'names: {names}')

# # 슬라이싱이란, 리스트에서 필요한 부분의 아이템만 뽑아내는 것
# animails = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'animails: {animails}')
# print(f'{animails[2:4]}')

# '''
# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
#  [3, 7, 1, 9, 5]
# '''
# maxNum = 0
# num = [3, 7, 1, 9, 5]
# print(f'num: {num}')
# print(f'maxNum: {num[3]}')

# '''
# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

# '''
# numData = int(input('숫자입력: '))
# sum = 0
# for num in range(1, numData +1 ):
#     sum += num
#     print(f'1부터 {numData}까지의 합: {sum}')

# '''
# 3. 리스트에 있는 숫자 중 짝수만 출력하기
#  [1,2,3,4,5,6]
# '''
# for num in range(1,7):
#     if num % 2 == 0:
#         print(f'짝수: {num}')


# '''
# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]
# '''
# num = [5,1,7,3]
# num.sort()
# print(num)

# '''
# 5. 리스트 숫자를 내림차순 정렬하기
#  [5,1,7,3]
# '''
# num = [5,1,7,3]
# num.sort(reverse = True)
# print(num)

# '''
# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]
# '''
# total = 0
# average = 0
# scores = [10,20,30]

# total = len(scores)
# average = total * len(scores)
# print(f'평균: {total / len(scores):.2f}')

'''
8. 1부터 100까지 숫자 중
3의 배수와 5의 배수 출력하기
'''
for number in range(1,101):
    if number % 3 == 0:
        print(f'3의 배수: {number}')
        
    if number % 5 == 0:
        print(f'5의 배수: {number}')
        