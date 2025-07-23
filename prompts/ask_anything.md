## project name ##
ask_anything

## metadata ##
- version: 001
- description: ask anything!

## system prompt ##
You are a helpful AI assistant.

## prompt1 ##
https://www.rootdata.com/Api/Doc 여기 api를 보고 간단한 프로그램을 짜줘
파이썬으로 짜고,
1. 프로젝트명과 해당 프로젝트의 (website 와 트위터 url)을 입력 받는다 https://api.rootdata.com/open/ser_inv 여기에서 id, name 들을 뽑는다 (type:1에 해당하는것들), 프로젝트명이 비슷해서 여러가지가 나올수가 있기때문임
2. https://api.rootdata.com/open/get_item 여기서 1에 나온 id를 토대로 데이터를 얻는다. 이때 website와 트위터를 둘다 얻는다 (없을경우 'N/A'로)
3. 1번의 입력으로 주어진 website 혹은 트위터(없을경우 'N/A'임)랑 비교해서 동일한 프로젝트인 경우 rootdata_url을 뽑는다.

참고로 api 사용법은 아래의 예시로 알수있음
search_url = 'https://api.rootdata.com/open/ser_inv'
search_headers = {
    'apikey': API_KEY_ROOTDATA,
    'Content-Type': 'application/json'
}
res = requests.post(search_url, json=search_payload, headers=search_headers)
data = res.json()

def get_project_ids(data):
    return [item.get('id') for item in data.get('data', []) if item.get('type') == 1]

def get_project_names(data):
    return [item.get('name') for item in data.get('data', []) if item.get('type') == 1]

project_ids = get_project_ids(data)
    project_names = get_project_names(data)

def fetch_project_detail(project_id):
    detail_url = 'https://api.rootdata.com/open/get_item'
    detail_payload = {
        'project_id': project_id,
        'include_team': True,
        'include_investors': True
    }
    detail_headers = {
        'apikey': API_KEY_ROOTDATA,
        'Content-Type': 'application/json'
    }
    resp = requests.post(detail_url, json=detail_payload, headers=detail_headers)
    return resp.json().get('data', {})

project_info = fetch_project_detail(pid)
social = project_info.get('social_media', {})
if social.get('website'):
    website = social.get('website')
if social.get('X'):
    twitter = social.get('X')
lines.append("")
rootdata_url = project_info.get('rootdataurl')