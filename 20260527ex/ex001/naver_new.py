import urllib.request
import datetime
import json

client_id = 'n2gVc82HBkJ_wwMEQ3PL'
Client_Secret = 'hqq7TOncDW'

# NAVER에서 데이터 가져오는 녀석
# 4번
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', Client_Secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            # decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것
            return response.read().decode('utf-8')

    except Exception as e:
        print(f'[{datetime.datetime.now()}]Error: {e}')
        return None
# NAVER에서 데이터 검색하는 녀석

# 3번
def getNaverSearch(node, srcText, start, display):
    # 대상(node), 검색어(srcTexat), 시작 번호(start), 가져올 개수(display)를 
    # 받아서 네이버 전용 주소를 만드는 함수를 시작한다.

    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'       # news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None

    else:
        return json.loads(responseDecode)

# 5번             
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

# 2번
def main():
    node = 'news'       # 크롤링 하는 대상(뉴스)
    srcText = input('검색어 입력: ')
    cnt = 0             # 뉴스 기사 번호를 매길 카운터
    jsonResult = []     # 최종 데이터 담을 빈 리스트


    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}'

    while jsonResponse != None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)


        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    # 파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}.json','w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)

# 1번
if __name__ == '__main__':
    main() 
# 파이썬 파일이 직접 실행되었을 때 main()이라는 함수를 실행해라