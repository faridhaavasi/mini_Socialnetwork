from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class HomeIndex(View):
    def get(self, request):
        return HttpResponse('hi cb')