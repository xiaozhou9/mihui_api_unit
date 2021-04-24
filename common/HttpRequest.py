import requests

class Httprequests(object):
    def __init__(self, url):
        self.url = url
        self.req = requests.session()
        self.header = {}

    def get(self, uri='', data='', params='', json='', headers=None, cookies=None):
        url = self.url + uri
        resopnse = self.req.get(url, data=data, params=params, json=json, headers=headers, cookies=cookies,
                                verify=False)
        return resopnse

    def post(self, uri='', data='', params='', json='', headers=None, cookies=None):
        url = self.url + uri
        response = self.req.post(url, data=data, params=params, json=json, headers=headers, cookies=cookies,
                                 verify=False)
        return response