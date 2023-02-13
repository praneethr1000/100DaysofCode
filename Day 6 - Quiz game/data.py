import requests
response_API = requests.get('https://opentdb.com/api.php?amount=10&category=20&type=boolean')
question_data = response_API.json()['results']
