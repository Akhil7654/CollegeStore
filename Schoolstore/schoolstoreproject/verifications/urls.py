from django.urls import path
from . import views

app_name='verifications'

urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('detail',views.detail,name="detail"),
    path('form',views.form,name="form")
]
