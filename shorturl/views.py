from django.conf.urls import url
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from shorturl.models import NewUrl
from redirecturl.models import Acces

from string import ascii_letters
from random import choice

is_not_authenticated = lambda user:not user.is_authenticated


@user_passes_test(is_not_authenticated, login_url='shorturl:user',redirect_field_name=None)
def homeView(request):
    return render(request,'shorturl/home.html')  


class LoginClassView(LoginView):
    template_name = 'shorturl/login.html'
    redirect_authenticated_user = True


class LogoutClassView(LogoutView):
    next_page = 'shorturl:home'

@user_passes_test(is_not_authenticated, login_url='shorturl:user',redirect_field_name=None)
def registerView(request):
    return render(request,'shorturl/register.html')


@user_passes_test(is_not_authenticated, login_url='shorturl:user',redirect_field_name=None)
def shorturlView(request):
    if request.method == 'GET':
        return redirect('shorturl:home')
    else:
        original_url = request.POST['url']
        characters = ascii_letters + '1234567890'
        new_url = 'http://127.0.0.1:8000/'
        url_id = ''
        while True:
            for i in range(5):
                url_id += choice(characters)
            if len(NewUrl.objects.filter(url_id=url_id))==0:
                break
        shorturl = NewUrl.objects.create(url_id=url_id,url_redirect=original_url)
        shorturl.save()
        new_url += url_id
        context = {'new_url':new_url}
        return render(request,'shorturl/shorturl.html',context=context)


@login_required
def userView(request):
    print('teste2')
    if request.method == 'GET':
        # Tab My URLs
        my_urls = NewUrl.objects.filter(url_user=request.user)
        url_data = []
        for url in my_urls:
            access_number = len(Acces.objects.filter(url=url))
            url_data.append((url,access_number))
        context = {'my_urls':url_data}
        return render(request,'shorturl/user.html',context=context)
    
    else:
        # Tab New URL
        original_url = request.POST['url']
        characters = ascii_letters + '1234567890'
        new_url = 'http://127.0.0.1:8000/'
        url_id = ''
        while True:
            for i in range(5):
                url_id += choice(characters)
            if len(NewUrl.objects.filter(url_id=url_id))==0:
                break
        shorturl = NewUrl.objects.create(url_id=url_id,url_redirect=original_url,url_user=request.user)
        shorturl.save()
        new_url += url_id
        
        # Tab My URLs
        my_urls = NewUrl.objects.filter(url_user=request.user)
        url_data = []
        for url in my_urls:
            access_number = len(Acces.objects.filter(url=url))
            url_data.append((url,access_number))
        context = {'my_urls':url_data}
        return render(request,'shorturl/user.html',context=context)


def urlDetailsView(request):
    url_id = request.POST['url']
    url = NewUrl.objects.get(url_id=url_id)

    if 'delete_action' in request.POST:
        url.delete()
        return redirect('shorturl:user')
    elif 'new_redirect' in request.POST:
        url.url_redirect = request.POST['new_redirect']
        url.save(update_fields=['url_redirect'])
        url_access = Acces.objects.filter(url=url_id)
        url_redirect = url.url_redirect
        access_number = len(url_access)
        template_option = 'pos_edit'
    else:
        url_access = Acces.objects.filter(url=url_id)
        url_redirect = url.url_redirect
        access_number = len(url_access)
        template_option = request.POST['template_option'] if 'template_option' in request.POST else 'details'

    context = {'url_id':url_id,'url_redirect':url_redirect,'url_access':url_access,'access_number':access_number,'template_option':template_option}
    return render(request,'shorturl/urlDetails.html',context=context)

"""
@login_required
def userView(request):
    return render(request,'shorturl/user.html')
"""