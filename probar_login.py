import json
import urllib.request
import urllib.error
import http.cookiejar
from getpass import getpass


URL_LOGIN = "http://localhost:8000/api/login"
CAMPO_USUARIO = "usuario"


def enviar_login(usuario, password):
   
    cookies = http.cookiejar.CookieJar()

    cliente = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cookies)
    )

    datos = {
        CAMPO_USUARIO: usuario,
        "password": password
    }

    contenido = json.dumps(datos).encode("utf-8")

    peticion = urllib.request.Request(
        URL_LOGIN,
        data=contenido,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        method="POST"
    )

    try:
        with cliente.open(peticion, timeout=10) as respuesta:
            return respuesta.status

    except urllib.error.HTTPError as error:
        return error.code


def comprobar(nombre, codigo_recibido, codigos_esperados):
    if codigo_recibido in codigos_esperados:
        print("[CORRECTO] " + nombre)
    else:
        print(
            "[FALLO] " + nombre
            + ". Código recibido: " + str(codigo_recibido)
            + ". Se esperaba: " + str(codigos_esperados)
        )


usuario = input("Usuario de prueba: ")
password = getpass("Contraseña correcta: ")
password_incorrecta = getpass("Contraseña incorrecta para probar: ")

if password == password_incorrecta:
    print("Las dos contraseñas deben ser diferentes.")
else:
    try:
        codigo = enviar_login(usuario, password)

        comprobar(
            "El login acepta las credenciales correctas",
            codigo,
            [200]
        )

        codigo = enviar_login(usuario, password_incorrecta)

        comprobar(
            "El login rechaza la contraseña incorrecta",
            codigo,
            [401, 403]
        )

    except urllib.error.URLError as error:
        print("No se pudo conectar con el backend: " + str(error.reason))