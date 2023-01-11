from django.urls import path

from core import views
from .views import GenerarIp,GeneraList,GeneraUp,GeneraDel

urlpatterns = [
    #core paths
    path('',GeneraList.as_view(),name='home'),
    path('create/',GenerarIp.as_view(),name='create'),
    path('update/<int:pk>/',GeneraUp.as_view(),name='update'),
    path('delete/<int:pk>/',GeneraDel.as_view(),name='delete'),
]
