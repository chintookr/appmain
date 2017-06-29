import create
from django.shortcuts import render_to_response,redirect
from django.utils import timezone
from .models import Appreq,User
from .forms import PostForm
from .forms import RegForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import subprocess
from calendar import monthrange
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@csrf_exempt
def appreq(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
            appreq = form.save(commit=False)
            appreq.published_date = timezone.now()
            appreq.save()
            create.main()
            return redirect('redirect')
    form = PostForm()
    return render_to_response( 'app/appreq.html', {'form':form}, RequestContext(request))
@csrf_exempt
def users(request):
    if request.method == 'POST':
      form = RegForm(request.POST)
      if form.is_valid():
          reg = form.save()
          reg.save()
    form = RegForm()
    return render_to_response( 'app/register.html', {'regform':form}, RequestContext(request))

def redirect(request):
    return render_to_response('app/redirect.html', {'redirect':redirect}, RequestContext(request))

def pagemain(request):
    return render_to_response('app/main.html', {}, RequestContext(request))

@login_required(login_url='/home.html')
def home(request):
    mail= request.user.email
    name= request.user.get_full_name
    dname=User.objects.get(name = name)
    dmail=User.objects.get(mail = mail)
    print('%s' %dname)
    if dname==name and dmail==mail:
      denied = Appreq.objects.filter(value='-1').order_by('published_date')
      tentative = Appreq.objects.filter(value='0').order_by('published_date')
      confirmed = Appreq.objects.filter(value='1').order_by('published_date')
      return render_to_response('app/home.html', {'request': request, 'user': request.user,'denied':denied,'tentative':tentative,'confirmed':confirmed}, RequestContext(request))
    print('No database match')
    return render_to_response('app/home.html', {'request': request, 'user': request.user}, RequestContext(request))

def auth_logout(request):
    logout(request)
    request.session.flush()
    return render_to_response('app/main.html', {}, RequestContext(request))
