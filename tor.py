import requests

print('''
  ,d                           
  88                           
MM88MMM ,adPPYba,  8b,dPPYba,  
  88   a8"     "8a 88P'   "Y8  
  88   8b       d8 88          
  88,  "8a,   ,a8" 88          
  "Y888 `"YbbdP"'  88 

          TOR Proxy Checker - Python Requests
''')

proxy = {
    'http':  'socks5://127.0.0.1:9050'
}   

url = 'http://httpbin.org/get'

r = requests.get(url, proxies=proxy)  
print('Tor IP:', r.json()['origin'])

r = requests.get(url)
print('normal IP:', r.json()['origin'])
