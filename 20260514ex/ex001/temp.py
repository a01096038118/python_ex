# split(쪼갠다.)
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'names: {names}')
print(f'names type: {type(names)}')

str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
splitedAStr = str.split("+")
print(f'spiltedAStr: {splitedAStr}')  # -> 리스트 타입으로 나옴
print(f' splitedAStr type: {type(splitedAStr)}')

splitedAStr =  tuple(splitedAStr)
print(f'splitedAStr: {splitedAStr}')
print(f'splitedAStr type: {type(splitedAStr)}')