from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import requests


USER_AUTH_URL = "https://mybook.ru/api/auth/"
USER_BOOKS_URL = "https://mybook.ru/api/bookuserlist/"


def index(request):
    return render(request, 'index.html')


def auth_user(request):
    user_email = request.POST["email"]
    user_password = request.POST["password"]

    auth_data = {
        "email": user_email,
        "password": user_password
    }

    session_cookie = requests.post(USER_AUTH_URL,
                                   json=auth_data).cookies["session"]

    response = HttpResponse()
    response.set_cookie("session", session_cookie)

    return response


def get_user_books(request):
    headers = {
        "Accept": "application/json; version=5",
        "Cookie": "session={}".format(request.COOKIES["session"])
    }

    books = requests.get(USER_BOOKS_URL, headers=headers).json()

    return JsonResponse(books)
