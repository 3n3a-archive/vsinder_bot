import requests

class SESSION():

    def __init__(self, headers):

        self.session = requests.Session()
        self.session.headers.update(headers)

    def get(self, url):
        
        return self.session.get(url)

    def post(self, url, json):
        
        return self.session.post(url, json=json)