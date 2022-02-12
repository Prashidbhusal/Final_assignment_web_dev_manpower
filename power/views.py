from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from login.auth import user_only
from .forms import FormVacancy
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'power/home.html')

def about(request):
    return render(request,'power/about.html')

def gallery(request):
    return render(request,'power/gallery.html')

def visa_p(request):
    return render(request,'power/visa_p.html')

def visa_step(request):
    return render(request,'power/visa_step.html')

def contact(request):
    if request.method == "GET":
        return render(request,'power/contact.html')
    else:
        name= request.POST.get('name')
        email= request.POST.get('email')
        message = request.POST.get('message')

        msg= Message()
        msg.name=name
        msg.email=email
        msg.query=message

        msg.save()
        
        messages.success(request, "Form submitted successfully. Thank you!")
        return redirect('/')
        


def req_doc(request):
    return render(request,'power/req_doc.html')
@login_required
@user_only
def jobs(request):
    vacancies= Vacancy.objects.all().order_by('-id')
    return render(request,'power/job.html',{'vacancies':vacancies})
@login_required()
@user_only
def jobform(request,id):
    if request.method == 'GET':
        form=FormVacancy()
        title= Vacancy.objects.get(id=id)
        vac= VacancyForm.objects.filter(vacancy=title)

        if vac.first():
            vac = True
            vac= VacancyForm.objects.get(vacancy=title)
            response=vac.response
        else:
            vac = False
            response=None
        return render(request,'power/jobform.html', {'form':form,'title':title, 'vacancy':vac, 'response':response})

    else:
        form = FormVacancy(request.POST, request.FILES)
        vacancy= Vacancy.objects.get(id=id)
        user= request.user


        if form.is_valid():
            ok= form.save(commit=False)
            ok.vacancy= vacancy
            ok.user= user

            ok.applied=True
            

            vtitle= vacancy.title
            ok.save()
            messages.success(request, "Form submitted successfully for "+ vtitle +". Thank you!")
            return redirect('/jobs')

        else:
            messages.add_message(request, messages.ERROR, 'Error in filling the form.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        


