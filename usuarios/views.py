from django.shortcuts import render, redirect
from django.http import HttpResponse

import requests
import json
import re

'''
Requerimientos:
- Para correr este codigo necesita el Id del coordinador: 
- El id es algo como: 43b2b051-8a54-4ae9-adf9-5f6eac5d6c2f
- Para esto pruebe el siguiente codigo en python:

coordinador='coordinador_rm'
superv=requests.get(url+'api/v1/supervisors?limit=10&offset=1', auth=(usuario,password))
for supervisor in superv.json()['Users']:
    if supervisor['UserName']==coordinador:
        supervisorId=supervisor['UserId']
        break
        
'''


# Create your views here.
def limpiaTexto(texto):
    '''Funcion para limpiar los caracteres como acentos y pasarlo a Survey Solutions'''
    texto = re.sub('[á|ä|à]', 'a', texto.lower())
    texto = re.sub('[é|ë|è]', 'e', texto)
    texto = re.sub('[í|ï|ì]', 'i', texto)
    texto = re.sub('[ó|ö|ò]', 'o', texto)
    texto = re.sub('[ú|ü|ù]', 'u', texto)
    texto = re.sub('ñ', 'n', texto)
    texto = re.sub(' ', '', texto)
    texto = re.sub('[-|.|,]', '', texto)
    return texto


def MuestraUsuarios(request):
    url = 'https://isarmiento-demo.mysurvey.solutions/'  # Pagina encuesta
    usuario_api = 'nachoapi'  # Usuario api
    password_api = 'Microdatos2020'  # Pass usuario api
    supervisorId = '43b2b051-8a54-4ae9-adf9-5f6eac5d6c2f'

    users = requests.get(url + 'api/v1/supervisors/' + supervisorId + '/interviewers?limit=100&offset=1',
                         auth=(usuario_api, password_api))
    users = users.json()['Users']
    info = []
    for usuario in users:
        name = usuario['UserName']
        userId = usuario['UserId']
        #        correo = usuario['Email']
        username = requests.get(url + 'api/v1/interviewers/' + userId, auth=(usuario_api, password_api))
        username = username.json()
        fullname = username['FullName']
        info.append({"usuario": name, "nombre": fullname})
    return render(request, "usuarios.html", {'contexto': info})


def CreaUsuarios(request):
    url = 'https://isarmiento-demo.mysurvey.solutions/'  # Pagina encuesta
    usuario_api = 'nachoapi'  # Usuario api
    password_api = 'Microdatos2020'  # Pass usuario api
    datos={'listo':False}
    try:

        nombre = limpiaTexto(request.POST['nombre'])
        apellidop = limpiaTexto(request.POST['apellidop'])
        apellidom = limpiaTexto(request.POST['apellidom'])
        rut = limpiaTexto(request.POST['rut'])
        print(nombre, apellidom, apellidop)
        # Nuevo Usuario maximo 15 caracteres
        nusuario = nombre[0] + apellidop
        npass = apellidop.title() + rut[0:6]
        ncompleto = nombre.title() + " " + apellidop.title() + " " + apellidom.title()

        if len(nusuario) > 15:
            nusuario = nusuario[0:15]
            npass = apellidop.title()[0:15] + rut[0:6]

        data = {
            "Role": "Interviewer",
            "UserName": nusuario,
            "FullName": ncompleto,
            "PhoneNumber": "1234567",
            "Email": "user@example.com",
            "Password": npass,
            "Supervisor": "coordinador_rm"
        }

        crear = requests.post(url + 'api/v1/users', json=data, auth=(usuario_api, password_api))
        print(crear.status_code)
        datos = {
            "UserName": nusuario,
            "FullName": ncompleto,
            "Password": npass,
            "listo": True
        }
    except:
        print("Clear")
    return render(request, "crear_usuarios.html",  {'contexto': datos})


def add_fin(request):
    return render(request, 'creado.html')
