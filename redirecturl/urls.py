from django.urls import path
from .views import redirectView

app_name = 'redirecturl'
urlpatterns = [
    path('<str:url_id>',redirectView),
]