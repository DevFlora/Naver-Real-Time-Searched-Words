import requests

myHeader = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

req = requests.get('https://api.signal.bz/news/realtime',headers=myHeader).json()

rankings = ""

for i in range(0, 10):
    title = req["top10"][i]['keyword']
    rankings += f'{i+1}. {title}\n'

print(rankings)
        
