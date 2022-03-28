from django.urls import path
from stac import views

app_name = 'stac'

urlpatterns = {
    path('심자윤/', views.yoon, name='심자윤'),
    path('박시은/', views.sieun, name='박시은'),
}