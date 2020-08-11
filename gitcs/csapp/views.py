from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print('再测试')
    print('新测试')
    print('没玩了')
    print('新增语句')
    print("hello")
    print('world')
    print('wocao')
    return HttpResponse('hello')
