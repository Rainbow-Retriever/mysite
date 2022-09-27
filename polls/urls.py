from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),  
]
# path 내에서 views.index라는 view 내부로 연결을 시켜준다.