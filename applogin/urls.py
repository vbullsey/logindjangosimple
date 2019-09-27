from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('amazon/', views.amazonView, name="amazon"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('registro/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='amazon'), name="logout"),

]