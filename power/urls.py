from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


def index(request):
    return HttpResponse("This is http responses from an app called products")


urlpatterns = [
    path('', views.index),
    path('about/',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('contact', views.contact,name='contact'),
    path('reqDoc', views.req_doc,name='reqDoc'),
    path('jobs', views.jobs,name='jobs'),
    path('visa_p', views.visa_p,name='visa_p'),
    path('visa_step', views.visa_step,name='visa_step'),
    path('jobform/<int:id>', views.jobform,name='jobform'),
    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name='power/changePassword.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
        template_name='power/changePasswordDone.html'), name='password_change_done'),


]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
        document_root=settings.STATIC_URL)
