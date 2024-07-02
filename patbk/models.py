from django.db import models
from django.contrib.postgres.fields import ArrayField
class patient(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    age=models.IntegerField()
    date=models.DateField()
    reson=models.CharField(max_length=100)
    pat_time=models.TimeField()
    visit_hos=models.CharField(max_length=100)
    visit_doc=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    status=models.IntegerField()
# Create your models here.
class docter(models.Model):
    name=models.CharField(max_length=20)
    # password=models.CharField(max_length=20)
    dpt=models.CharField(max_length=20)
    exp=models.IntegerField()
    rating=models.IntegerField()
    img=models.FileField()
    hospital=models.CharField(max_length=100)
    con_no=models.IntegerField()
    email=models.CharField(max_length=100)
    st_time=models.TimeField()#start time of docter
    end_time=models.TimeField()#end time of docter
    day_avail=models.CharField(max_length=10)# in this i create monday to sunday as number 1 to 7 and its store in string formation by string concantination method
class hospital(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cno=models.IntegerField()
    email=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    #locationlink=models.CharField(max_length=100)
    image=models.FileField()
    rating=models.IntegerField()
    long=models.FloatField()
    lat=models.FloatField()