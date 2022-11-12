from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.

@csrf_exempt
def home(request):
    return JsonResponse({'success': False, 'msg': "Failed to Create Account"})

@csrf_exempt
def getId(request, id=0):
    return JsonResponse({'success': False, 'msg': id})