import requests

token = "9OdHFciJquUwpAXNl4lavsxdPjClLckNMrfzI9lE04K"
url = "https://notify-api.line.me/api/notify"
def lineNotifyMessage(msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code


def lineNotifyImage(msg, picURI):
    headers = {
        "Authorization": "Bearer " + token
    }

    payload = {'message': msg}
    files = {'imageFile': open(picURI, 'rb')}
    r = requests.post(url, headers=headers, params=payload, files=files)
    return r.status_code


#msg = "Hello Python"
#picURI = "girl.jpg"
#lineNotifyImage(msg, picURI)
