import requests


def get_razas():
    r = requests.get("https://dog.ceo/api/breeds/list/all")
    print(r.status_code)
    print (r.text)
    