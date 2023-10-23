import requests
import json
from .models import ServicioApi
from django.core.mail import send_mail
from django.conf import settings

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

def enviar_correo():

    subject = 'Asunto del correo'
    message = 'Este es el contenido del correo.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['cl.cortesp89@gmail.com']

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
