# '''
# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
# '''
# nums = [3, 7, 1, 9, 5]
# maxNum = 0
# for num in nums:
#     # "nums 리스트 안의 숫자를 하나씩 꺼내 반복한다

#     if num > maxNum: 
#          #"현재 숫자(num)가 지금까지의 최대값(maxNum)보다 크면
#         maxNum = num     # maxNum:  num:  > maxNum =  
     
# print(f'maxNum: {maxNum}')

# nums = [4, 5, 2, 7, 8, 3]
# maxNum = 0
# for num in nums:
#     if num > maxNum:
#         maxNum = num
# print(f'maxNum: {maxNum}')

# ----------------------------------------------------
# '''
# 2. 사용자에게 숫자 입력받아서 1부터 입력한 숫자까지 합계 출력하기 ( 5 )
# '''
# userInputNum = int(input('입력하세요: '))
# total = 0
# # 반복하면서 숫자를 계속 더할 준비
# for num in range(1, userInputNum +1):
#     total += num

# print(f'total: {total}')

# # 숫자를 입력받아 1부터 입력한 숫자까지의 짝수 합 구하기

# userInputNum = int(input('입력하세요: '))
# total = 0
# for number in range(1,userInputNum +1):
#     if number % 2 == 0: # -> if number % 2 == 1: # 홀수라면
#         total += number
# print(f'total: {total}')
# --------------------------------------
# '''
# 3. 리스트에 있는 숫자 중 짝수만 출력하기
#  [1,2,3,4,5,6]
# '''
# nums = [1,2,3,4,5,6]
# for num in nums:
#     if num % 2 == 0:
#         print(f'num: {num}')
#----------------------------------------
# '''
# 4. 리스트 숫자를 오름차순 정렬하기 [5,1,7,3]
# '''
# num = [5,1,7,3]
# num.sort()
# print(f'num: {num}')

#----------------------------------------
# '''
# 5. 리스트 숫자를 내림차순 정렬하기 [5,1,7,3]
# '''
# num = [5,1,7,3]
# num.sort(reverse = True)
# print(f'num: {num}')

#----------------------------------------
# '''
# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]
# '''
# nums = [10,20,30]
# total = 0
# average = 0
# for num in nums:
#     total += num
#     # "total에 num을 더해서 다시 total에 저장한다"
# average = total / len(nums)

# print(f'total: {total}')
# print(f'average: {average}')

#----------------------------------------
# '''
# 7. 리스트에서 가장 작은 숫자 찾기 (min() 사용 금지)
# '''
# nums = [3, 7, 1, 9, 5]
# minNum = nums[0]
# for num in nums:
#     if num < minNum:
#         minNum = num
#         print(f'minNum: {minNum}')

#----------------------------------------
# '''
# 8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기
# '''
# for num in range(1,101):
#     if num % 3 == 0:
#         print(f'3의 배수: {num}')

# for num in range(1,101):
#     if num % 5 == 0:
#         print(f'5의 배수: {num}')
#----------------------------------------
# '''
# 9. 사용자가 입력한 숫자를 리스트에 저장하다가 0 입력하면 종료 후 리스트 출력하기
#    [입력: 3 ,입력: 7, 입력: 2 ,입력: 0] -> [3, 7, 2]
# '''
# nums = []

# while True:
#      userInputNumber = int(input('숫자입력: '))
#      if  userInputNumber == 0:
#           break
     
#      nums.append(userInputNumber)
#      print(f'nums: {nums}')

# num1 = 10
# num2 = num1
# print(f'num1: {num1}')      # 10
# print(f'num2: {num2}')      # 10

# num1 = 100
# print(f'num1: {num1}')      # 100
# print(f'num2: {num2}')      # 10

# nums1 = [1, 2, 3]
# nums2 = nums1
# print(f'nums1: {nums1}')    # [1, 2, 3]
# print(f'nums2: {nums2}')    # [1, 2, 3]

# nums1[0] = 100
# print(f'nums1: {nums1}')    # [100, 2, 3]
# print(f'nums2: {nums2}')    # [100, 2, 3]

# for idx, num in enumerate(nums1): 
#    nums2[idx] = num
# "nums1의 값들을 하나씩 꺼내면서
# 번호(index)는 idx에 저장하고 값은 num에 저장한 뒤,
# nums2의 같은 위치에 넣어라"
