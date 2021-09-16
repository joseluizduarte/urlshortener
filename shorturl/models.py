from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class NewUrl(models.Model):
    url_id = models.CharField(max_length=5,primary_key=True)
    url_redirect = models.URLField()
    url_user = ForeignKey(User,null=True,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.url_id
