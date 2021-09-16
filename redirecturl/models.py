from django.db import models
from shorturl.models import NewUrl

class Acces(models.Model):
    url = models.ForeignKey(NewUrl,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()