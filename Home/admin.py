from django.contrib import admin
from Home.models import UserData, CitizenRequest, CorporateRequest
# Register your models here.
admin.site.register(UserData)
admin.site.register(CitizenRequest)
admin.site.register(CorporateRequest)
