from django.urls import path
from schoolstoreapp import views

app_name="schoolstoreapp"

urlpatterns = [
    path('',views.home,name="home"),
]
