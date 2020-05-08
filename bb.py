import requests

headers = {
    'authority': 'www.bigbasket.com',
    'origin': 'https://www.bigbasket.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko)',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-dest': 'empty',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': <token>,
    'dnt': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.bigbasket.com/basket/?ver=1',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '<cookie>',
}
data = {
  'addr_id': '<id>'
}
response = requests.post('https://www.bigbasket.com/co/update-po/', headers=headers, data=data)

res = response.json()
print(res)
if response.status_code != 200 or res['status'] != 'failure':
    headers = {
        'Content-type': 'application/json',
    }
    data = '{"text":"Slots are open now check Bigbasket! %s"}' % str(res)
    response = requests.post('https://hooks.slack.com/services/<generated-token>', headers=headers, data=data)
