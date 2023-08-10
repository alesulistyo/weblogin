from django.db import connection
from django.shortcuts import render, redirect
import hashlib


# Create your views here.
def index(request):
    context = {
        "title": "CHRONICLE",
    }
    return render(request, "home.html", context)


def signin(request):
    context = {
        "title": "CHRONICLE",
    }
    return render(request, "signin.html", context)


def signin_fail(request):
    context = {
        "title": "CHRONICLE",
    }
    return render(request, "signin_fail.html", context)


def submit(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        h = hashlib.new("SHA256")
        h.update(password.encode())
        hashed = h.hexdigest()

        cursor = connection.cursor()
        query = "SELECT * FROM account WHERE username = %s AND password = %s"
        cursor.execute(query, [username, hashed])

        if cursor.fetchall():
            cursor.close()
            request.session["username"] = username
            return redirect("/welcome")
        else:
            cursor.close()
            return redirect("/signin/fail")

    return render(request, "signin.html")


def signup(request):
    context = {
        "title": "CHRONICLE",
    }
    return render(request, "signup.html", context)


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        h = hashlib.new("SHA256")
        h.update(password.encode())
        hashed = h.hexdigest()

        cursor = connection.cursor()
        query = "SELECT * FROM account WHERE username = %s"
        cursor.execute(query, [username])

        if cursor.fetchall():
            cursor.close()
            return redirect("/signup/fail")
        else:
            cursor = connection.cursor()
            query = "INSERT INTO account(username, password) VALUES (%s, %s)"
            cursor.execute(query, [username, hashed])
            cursor.close()
            return redirect("/signup/success")

    return render(request, "signin.html")


def signup_success(request):
    context = {
        "title": "CHRONICLE",
    }
    return render(request, "signup_success.html", context)


def signup_fail(request):
    context = {
        "title": "CHRONICLE",
    }
    return render(request, "signup_fail.html", context)
