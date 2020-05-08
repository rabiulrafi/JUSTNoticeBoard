from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.



def index(request):
	notices=Notice.objects.all()
	return render(request,'noticeboard/index.html',{'notices':notices})



def uploadNotice(request):
	
	if request.method=='POST':
		form=NoticeUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:

		form= NoticeUpload()

	return render(request,'noticeboard/upload.html',{'form':form})

