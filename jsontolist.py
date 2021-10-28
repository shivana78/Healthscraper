import json
with open('text-query-tweets.json', 'r') as file:
    data = json.load(file)
    print(data['list'])
