from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index),
    path("signin/", views.signin),
    path("signin/fail/", views.signin_fail),
    path("signin/submit/", views.submit),
    path("signup/", views.signup),
    path("signup/fail/", views.signup_fail),
    path("signup/register/", views.register),
    path("signup/success/", views.signup_success),
    path("welcome/", include("welcome.urls")),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
