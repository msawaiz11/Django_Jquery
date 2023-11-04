from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('send_data/', views.send_data, name='send_data'),
    path('download_docx/', views.download_docx, name='download_docx')
]