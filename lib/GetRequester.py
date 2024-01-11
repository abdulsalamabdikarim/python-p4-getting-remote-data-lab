import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        # print(response.content)
        return response.content

    def load_json(self):
        data = json.loads(self.get_response_body())
        # print(data)
        # print(json.dumps(data, indent=4, sort_keys=True))
        return data

#test example below 
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()
