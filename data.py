import requests

params = {
    'amount': 10,
    'type': 'boolean',
}
response = requests.get('https://opentdb.com/api.php', params=params)
response.raise_for_status()
response_json = response.json()

question_data = response_json['results']
