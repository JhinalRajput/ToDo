from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('/', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout',views.logout, name="logout"),
    path('error', views.error, name="error")
]
