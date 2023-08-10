from django.contrib.auth import logout
from django.db import connection
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    username = request.session.get("username", None)

    cursor = connection.cursor()
    query = "SELECT * FROM account WHERE username = %s"
    cursor.execute(query, [username])

    if cursor.fetchall():
        cursor.close()
    else:
        cursor.close()
        return redirect("/")

    logout(request)

    context = {
        "title": "CHRONICLE",
        "username": username,
    }
    return render(request, "welcome.html", context)


def userlogout(request):
    logout(request)
    return redirect("/")
