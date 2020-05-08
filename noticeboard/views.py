from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from JUSTNoticeBoard import helpers
# Create your views here.



def index(request):
	notices=Notice.objects.all()
	notices = helpers.pg_records(request, notices, 20)

	return render(request,'noticeboard/index.html',{'notices':notices})

def dept(request,str):
	notices=Notice.objects.filter(department=str)

	return render(request,'noticeboard/dept.html',{'notices':notices,'str':str})


@login_required(login_url='/login/')
def uploadNotice(request):
	
	if request.method=='POST':
		form=NoticeUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:

		form= NoticeUpload()

	return render(request,'noticeboard/upload.html',{'form':form})

