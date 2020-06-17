from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import auth
from .users import Login, CitRequest, CorRequest
from .models import UserData, CorporateRequest, CitizenRequest
from django.utils.html import format_html


def index(request):
    return render(request, 'index.html', )


"""def citizen(request, user):
    if user:
        messages.info(request, user.name)
        messages.info(request, 'Sign In Successful!')
        return render(request, 'citizen.html', )
    else:
        return redirect('/')"""


def citizen(request):
    return render(request, 'citizen.html', )


def police(request):
    return render(request, 'police.html', )


def corporate(request):
    return render(request, 'corporate.html', )


def authority(request):
    return render(request, 'authority.html', )


def essential(request):
    return render(request, 'essential.html', )


def approval(request):
    return render(request, 'approval.html', )


def bulk(request):
    return render(request, 'bulk.html', )


def locality(request):
    return render(request, 'locality.html', )


def locality_set(request):
    return render(request, 'locality_set.html', )


def signIn(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            req_user = UserData.objects.get(email=email)
            # user = auth.authenticate(email=email, password=password)
            if req_user is not None:
                # auth.login(request, user)
                if req_user.password == password:
                    messages.success(request, 'Sign In Successful!')
                    if req_user.usertype == "Citizen":
                        # return citizen(request, req_user)
                        return redirect('citizen')
                    if req_user.usertype == "Police":
                        return redirect('police')
                    if req_user.usertype == "Corporate":
                        return redirect('corporate')
                    if req_user.usertype == "Authority":
                        return redirect('authority')
                    if req_user.usertype == "Essential":
                        return redirect('essential')
                else:
                    messages.info(request, 'Password wrong')
                    return redirect('/')
            else:
                messages.info(request, 'Email is not registered')
                return redirect('/')
        else:
            messages.info(request, 'Could not read email or password')
            return redirect('/')
    else:
        return render(request, 'index.html')


def signUp(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Sign Up Successful!')
            return redirect('/')
        else:
            messages.info(request, 'Sign Up Failed!')
            return redirect('/')
    else:
        return render(request, 'index.html')


def citReq(request):
    if request.method == "POST":
        form = CitRequest(request.POST)
        if form.is_valid():
            req = form.save()
            messages.info(request, 'Request Successful!')
            messages.info(request, 'Your CNR number is ' + str(req.id) + '.')
            return redirect('citizen')
        else:
            messages.info(request, 'Request Failed!')
            return redirect('citizen')
    else:
        return render(request, 'citizen.html')


def citStatus(request):
    if request.method == "POST":
        aadhaar = request.POST['aadhaar']
        cnr_num = request.POST['cnr_num']
        if aadhaar and cnr_num:
            req = CitizenRequest.objects.get(id=cnr_num)
            # user = auth.authenticate(email=email, password=password)
            if req is not None:
                # auth.login(request, user)
                if req.aadhaar == int(aadhaar):
                    messages.info(request, 'Your request is ' + str(req.status) + '.')
                    if req.status == "Approved":
                        messages.info(request, format_html('<div style="text-align:center;">'
                                                           '<a href="#" style="text-decoration:underline;'
                                                           ' color:white;">Download Pass</a></div>'))
                    return redirect('citizen')
                else:
                    messages.info(request, 'Aadhaar does not match')
                    return redirect('citizen')
            else:
                messages.info(request, 'No such request.')
                return redirect('citizen')
        else:
            messages.info(request, 'Could not read Aadhaar or CNR number.')
            return redirect('citizen')
    else:
        return render(request, 'citizen.html')

def corReq(request):
    if request.method == "POST":
        form = CorRequest(request.POST)
        if form.is_valid():
            req = form.save()
            messages.info(request, 'Request Successful!')
            messages.info(request, 'Your Bulk Request ID is ' + str(req.id) + '.')
            return redirect('corporate')
        else:
            messages.info(request, 'Request Failed!')
            return redirect('corporate')
    else:
        return render(request, 'corporate.html')


def corStatus(request):
    if request.method == "POST":
        aadhaar = request.POST['aadhaar']
        req_id = request.POST['req_id']
        if aadhaar and req_id:
            req = CorporateRequest.objects.get(id=req_id)
            # user = auth.authenticate(email=email, password=password)
            if req is not None:
                # auth.login(request, user)
                if req.aadhaar == int(aadhaar):
                    messages.info(request, 'Your request is ' + str(req.status) + '.')
                    if req.status == "Approved":
                        messages.info(request, format_html('<div style="text-align:center;">'
                                                           '<a href="#" style="text-decoration:underline;'
                                                           ' color:white;">Download Pass</a></div>'))
                    return redirect('corporate')
                else:
                    messages.info(request, 'Aadhaar does not match')
                    return redirect('corporate')
            else:
                messages.info(request, 'No such request.')
                return redirect('corporate')
        else:
            messages.info(request, 'Could not read Aadhaar or Bulk request ID.')
            return redirect('corporate')
    else:
        return render(request, 'corporate.html')


def essReq(request):
    if request.method == "POST":
        form = CitRequest(request.POST)
        if form.is_valid():
            req = form.save()
            messages.info(request, 'Request Successful!')
            messages.info(request, 'Your CNR number is ' + str(req.id) + '.')
            return redirect('essential')
        else:
            messages.info(request, 'Request Failed!')
            return redirect('essential')
    else:
        return render(request, 'essential.html')


def essStatus(request):
    if request.method == "POST":
        aadhaar = request.POST['aadhaar']
        cnr_num = request.POST['cnr_num']
        if aadhaar and cnr_num:
            req = CitizenRequest.objects.get(id=cnr_num)
            # user = auth.authenticate(email=email, password=password)
            if req is not None:
                # auth.login(request, user)
                if req.aadhaar == int(aadhaar):
                    messages.info(request, 'Your request is ' + str(req.status) + '.')
                    if req.status == "Approved":
                        messages.info(request, format_html('<div style="text-align:center;">'
                                                           '<a href="#" style="text-decoration:underline;'
                                                           ' color:white;">Download Pass</a></div>'))
                    return redirect('essential')
                else:
                    messages.info(request, 'Aadhaar does not match')
                    return redirect('essential')
            else:
                messages.info(request, 'No such request.')
                return redirect('essential')
        else:
            messages.info(request, 'Could not read Aadhaar or CNR number.')
            return redirect('essential')
    else:
        return render(request, 'essential.html')


def viewCorporateTable(request):
    query_results = CorporateRequest.objects.all()
    context = {'query_results': query_results}
    return render(request, 'approve_corporate.html', context)


def approveCom(request, id=None):
    if id:
        request_obj = CorporateRequest.objects.get(id=id)
        request_obj.status = "Approved"
        request_obj.save(update_fields=['status'])
        return redirect('approve_corporate')
    else:
        return redirect('approve_corporate')


def rejectCom(request, id=None):
    if id:
        request_obj = CorporateRequest.objects.get(id=id)
        request_obj.status = "Rejected"
        request_obj.save(update_fields=['status'])
        return redirect('approve_corporate')
    else:
        return redirect('approve_corporate')


def viewCitizenTable(request):
    query_results = CitizenRequest.objects.all()
    context = {'query_results': query_results}
    return render(request, 'approve_citizen.html', context)


def approveCit(request, id=None):
    if id:
        request_obj = CitizenRequest.objects.get(id=id)
        request_obj.status = "Approved"
        request_obj.save(update_fields=['status'])
        return redirect('approve_citizen')
    else:
        return redirect('approve_citizen')


def rejectCit(request, id=None):
    if id:
        request_obj = CitizenRequest.objects.get(id=id)
        request_obj.status = "Rejected"
        request_obj.save(update_fields=['status'])
        return redirect('approve_citizen')
    else:
        return redirect('approve_citizen')
