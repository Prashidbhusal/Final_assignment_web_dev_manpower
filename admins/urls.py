from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.adminhome,name=''),
    path('totaluser', views.totalusers,name='totaluser'),
    path('totalvacancy', views.totalvacancy,name='totalvacancy'),
    path('msg-requests', views.msgrequest,name='msgrequest'),
    path('applied-vacancy', views.appliedVacancy,name='appliedvacancy'),
    path('applied-detail/<int:id>', views.appliedDetail,name='appliedDetail'),
    path('msg-detail/<int:id>', views.msgDetail),
    path('addvacancy', views.addVacancy,name='addvacancy'),
    path('editvacancy/<int:id>', views.editVacancy,name='editvacancy'),
    path('dash', views.adminhome),


    
]