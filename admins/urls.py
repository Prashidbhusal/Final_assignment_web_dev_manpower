from django.urls import path
from .import views

urlpatterns = [
    path('', views.adminhome),
    path('totaluser', views.totalusers),
    path('totalvacancy', views.totalvacancy),
    path('msg-requests', views.msgrequest),
    path('applied-vacancy', views.appliedVacancy),
    path('applied-detail/<int:id>', views.appliedDetail),
    path('msg-detail/<int:id>', views.msgDetail),
    path('addvacancy', views.addVacancy),
    path('editvacancy/<int:id>', views.editVacancy),
    path('dash', views.adminhome),


    
]