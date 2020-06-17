from django.db import models


class UserData(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    aadhaar = models.IntegerField(primary_key=True)
    usertype = models.CharField(max_length=10)


class CitizenRequest(models.Model):

    aadhaar = models.IntegerField()
    req_date = models.DateField()
    req_time = models.TimeField()
    req_duration = models.IntegerField()
    status = models.CharField(max_length=15, default="Pending")


class CorporateRequest(models.Model):

    aadhaar = models.IntegerField()
    organization_name = models.CharField(max_length=50)
    cin_no = models.CharField(max_length=30)
    industry_type = models.CharField(max_length=30)
    num_requested = models.IntegerField()
    req_date = models.DateField()
    req_time = models.TimeField()
    req_duration = models.IntegerField()
    status = models.CharField(max_length=15, default="Pending")

