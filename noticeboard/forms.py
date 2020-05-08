from django import forms
from .models import *

class NoticeUpload(forms.ModelForm):
	class Meta:
		model= Notice
		fields= ['user','title','department','pdf']