from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Docker-Jenkins 배포 자동화 테스트 - 02")
