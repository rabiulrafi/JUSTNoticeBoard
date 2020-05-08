from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension

# Create your models here.

class Notice(models.Model):
	DEPT_CHOICES = (
    ("CSE", "CSE"),
    ("EEE", "EEE"),
    ("BME", "BME"),
    ("PME", "PME"),
    ("TE", "TE"),
    ("ChE", "ChE"),
    ("EST", "EST"),
    ("NFT", "NFT"),
    ("APPT", "APPT"),
    ("CDM", "CDM"),
    ("FMB", "FMB"),
    ("GEBT", "GEBT"),
    ("Pharmacy", "Pharmacy"),
    ("MB", "MB"),
    ("PESS", "PESS"),
    ("NHS", "NHS"),
    ("English", "English"),
    ("AIS", "AIS"),
    ("Management", "Management"),
    ("F&B", "F&B"),
    ("Marketing", "Marketing"),
	)
	user= models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
	title= models.CharField(max_length=200, null=True)
	department=models.CharField(max_length=100,choices=DEPT_CHOICES)
	publish=models.DateTimeField(auto_now_add=True)
	pdf = models.FileField(upload_to='book/pdfs/',validators=[validate_file_extension])

	class Meta:
		ordering = ['-publish']

	def __str__(self):
		return self.title
