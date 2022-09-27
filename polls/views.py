from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")
# view 내부의 index 함수에서는 아래와 같은 응답을 클라이언트에게 전달해준다. 