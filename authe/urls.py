from django.urls import path
from authe.views import register_view, login_view, logout_view, home_view
app_name = 'authe'
urlpatterns = [
    path(route='', view=register_view, name="register"),
    path(route='login/', view=login_view, name="login"),
    path(route='logout/', view=logout_view, name="logout"),
    path(route='home/', view=home_view, name="home"),
]
