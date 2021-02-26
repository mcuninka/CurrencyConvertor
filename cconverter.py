import requests
import json

curr_in = input().lower()
curr_rates = dict()
url = f'http://www.floatrates.com/daily/{curr_in}.json'
response = requests.get(url)
json_data = json.loads(response.text)
if curr_in != 'eur':
    curr_rates['eur'] = json_data['eur']['rate']
if curr_in != 'usd':
    curr_rates['usd'] = json_data['usd']['rate']

while True:
    curr_out = input().lower()
    if curr_out != '':
        amount = int(input())
        print('Checking the cache…')
        if curr_out not in curr_rates:
            print('Sorry, but it is not in the cache!')
            rate = json_data[f'{curr_out}']['rate']
            money = amount * rate
            curr_rates[curr_out] = rate
        else:
            print('Oh! It is in the cache!')
            money = amount * curr_rates[curr_out]
        print('You received ' + str(round(money, 2)) + ' ' + curr_out.upper())
    else:
        break
