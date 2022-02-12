from django.shortcuts import render, redirect, HttpResponseRedirect
from power.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Vacancy_Form
from .filters import VacancyFilter

# Create your views here.

def adminhome(request):
    totalusers= User.objects.filter(is_staff=False).count()
    totalvacancy= Vacancy.objects.all().count()
    vacancyapplied=VacancyForm.objects.all().count()
    msgreq = Message.objects.all().count()
    context= {'totusers':totalusers,
                'totvacancy':totalvacancy,
                'totvacancyapp': vacancyapplied,
                'msgreq':msgreq}
    return render(request, 'admins/adminDashboard.html', context)


def totalusers(request):
    totuser= User.objects.filter(is_staff=False)
    context= {'totuser':totuser}
    return render(request, 'admins/totaluser.html', context)


def totalvacancy(request):

    totalvacancy= Vacancy.objects.all().order_by('-id')
    totalvacancy_filter= VacancyFilter(request.GET, queryset=totalvacancy)
    total_final=totalvacancy_filter.qs

    context= {'total_final':total_final,'totalvacancy_filter':totalvacancy_filter}
    return render(request, 'admins/totalvacancy.html', context)

def msgrequest(request):
    totalmsg_sn= Message.objects.filter(seen=True).order_by('-id')
    totalmsg_us= Message.objects.filter(seen=False).order_by('-id')
    context= {'totalmsg_sn':totalmsg_sn,'totalmsg_us':totalmsg_us}
    return render(request, 'admins/totalmsg.html', context)

def appliedVacancy(request):
    totapp_sn= VacancyForm.objects.filter(seen=True).order_by('-id')
    totapp_us= VacancyForm.objects.filter(seen=False).order_by('-id')
    context= {'totapp_sn':totapp_sn,'totapp_us':totapp_us}
    return render(request, 'admins/appliedvacancy.html', context)


def vacancyDetail(request,id):
    pass

def msgDetail(request,id):
   
    form= Message.objects.get(id=id)
    form.seen=True
    form.save()

    return render(request,'admins/msgdetail.html',{'form':form})
    
    

def appliedDetail(request,id):
    if request.method == 'GET':
        form= VacancyForm.objects.get(id=id)
        form.seen=True
        form.save()

        return render(request,'admins/applieddetail.html',{'form':form})
    else:
        form= VacancyForm.objects.get(id=id)
        response= request.POST.get('response')
        form.response=response
        form.save()
        messages.success(request,'Response saved Successfull.')
        return redirect('/admins/applied-vacancy')
        

def addVacancy(request):
    if request.method == 'GET':
        form= Vacancy_Form
        return render(request,'admins/addVacancy.html',{'form':form})
    else:
        form= Vacancy_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Vacancy added Successfully.')
            return redirect('/admins/totalvacancy')
        else:
            messages.error(request,'Error!!.')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def editVacancy(request,id):
    vac = Vacancy.objects.get(id=id)
    if request.method == 'POST':
        form = Vacancy_Form(request.POST,instance=vac)
        if form.is_valid():
            form.save()
            messages.success(request,'Vacancy updated successfully.')
            return redirect('/admins/totalvacancy')

    context = {
        'form': Vacancy_Form(instance=vac),
        
    }
    return render(request, 'admins/editVacancy.html', context)







