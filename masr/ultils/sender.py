import requests

def gen_sender(dtypes, target):
    def sender(data):
        if dtypes == 'MAS':
            headers = {'Content-Type': 'application/json'}
            return requests.post(target, json=data, headers = headers)
        else:
            ...
    return sender