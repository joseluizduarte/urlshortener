from django.shortcuts import render, redirect
from shorturl.models import NewUrl
from redirecturl.models import Acces

def redirectView(request,url_id):
    print('teste1')
    print(url_id)
    new_url = NewUrl.objects.get(url_id=url_id)
    acces = Acces.objects.create(url=new_url,ip=request.META['REMOTE_ADDR'])
    acces.save()
    url_redirect = new_url.url_redirect
    return redirect(url_redirect)
