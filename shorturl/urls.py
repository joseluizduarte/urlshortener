from django.urls import path
from .views import homeView, LoginClassView, LogoutClassView, registerView, shorturlView, userView, urlDetailsView

app_name = 'shorturl'
urlpatterns = [
    path('',homeView,name='home'),
    path('login',LoginClassView.as_view(),name='loginPage'),
    path('logout',LogoutClassView.as_view(),name='logoutPage'),
    path('register',registerView,name='register'),
    path('shorturl',shorturlView,name='shorturl'),
    path('user',userView,name='user'),
    path('urlDetails',urlDetailsView,name='urlDetails'),
]