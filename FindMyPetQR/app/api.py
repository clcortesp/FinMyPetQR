import requests
import json
from .models import ServicioApi

def getToken():
    token = ServicioApi.objects.get(name = "Token")
    url = token.url

    payload={'client_id': token.client_id,
    'grant_type': token.grant_type,
    'client_secret': token.client_secret,
    'username': token.username,
    'password': token.password}
    files=[

    ]
    headers = {
        #'Cookie': 'BrowserId=W7VZ_QRIEeuNf4VeKfQx0A; CookieConsentPolicy=0:0'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    x = response.text
    y = json.loads(x)
    print(y["access_token"])
    return y["access_token"]

