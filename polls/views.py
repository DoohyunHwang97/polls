from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 polls에 오신것을 환영합니다.")


from django.shortcuts import render

# Create your views here.
