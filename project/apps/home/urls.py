from django import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import TemplateView, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = "home"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/index.html"), name="index"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("registro/", RegistroPagina.as_view(), name="registro"),
    path("edicionPerfil/", UsuarioEdicion.as_view(), name="edicionPerfil"),
    path("passwordCambio/", CambioPassword.as_view(), name="passwordCambio"),
    path("passwordExitoso/", views.password_exitoso, name="passwordExitoso"),
    path("about/", views.about, name="about"),
] + staticfiles_urlpatterns()
