from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print("不使用免密登录的第二次推送")
    print('不适用免密登陆了')
    print('今天最后测试')
    print('争取成功')
    print('再测试')
    print('新测试')
   
    print('新增语句')
    print("hello")
    print('world')
    print('wocao')
    return HttpResponse('hello')
