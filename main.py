import requests
val = "PLN"
date = "20200302"
url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date=20200302&json"
r = requests.get(url)
if r.status_code == 200:
   data = r.json()
   print(data)
else:
   print("Помилка")