import urllib.request
import datetime
import json


client_id = 'n2gVc82HBkJ_wwMEQ3PL'
Client_Secret = 'hqq7TOncDW'

def getRequestUrl(url):
    req = urllib.request. Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client_Secret-Id', Client_Secret)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SECCESS!!')
            return response.read().decode('utf-8')
        
    except Exception as e:
        print(f'[{datetime.datetime.now()}]Error: {e}')
        return None




def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display{display}'
    
    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None
    
    else:
        return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['org_link']
    link = post['link']



def main():
    node = 'news'
    scrText = input('검색어 입력: ')
    cnt = 0
    jsonResult = []

if __name__ == '__main__':
    main()
