from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from .models import restaurants
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
# Create your views here.
from rest_framework import status
def test(request):
     
    return render(request,'index.html')

def login_view(request):
    return render(request,'login.htm')

def order_view(request):
    return render(request,'order.html')

def register(request):
    name=request.POST.get('name', None)
    email=request.POST.get('eml',None)
    pwd=request.POST.get('pwd',None)
    uname=request.POST.get('uname',None)

    if User.objects.filter(username=uname).exists():
        return HttpResponse("User already available")
    else:
        user_obj=User.objects.create(username=uname,first_name=name,password=pwd,email=email)
        user_obj.set_password(pwd)
        user_obj.save()
        auth.login(request,user_obj)
        return HttpResponse("You are loffed in successfully")
def order(request ):
    name=request.POST.get('name', None)
    rname = request.POST.get('rname', None)
    pnumber=request.POST.get('pnumber',None)
    uname=request.POST.get('uname',None)
    odate = request.POST.get('odate', None)
    dishp = request.POST.get('food', None)
    dl=request.POST.get('fun', None)
    restaurants_obj=restaurants.objects.create(restaurant_name=name,restaurant_address=rname,user_who_placed_order=uname,date=odate,dishes_name=dishp,dishes_price=dl)
    restaurants_obj.save()

    return HttpResponse("You are ordered  successfully")


def login(request):
    uname=request.POST.get('uname',None)
    pwd=request.POST.get('pwd',None)
    
    uobj= auth.authenticate(request,username=uname,password=pwd)
    if uobj:
        return HttpResponse("Logged in...")
    else:
        return HttpResponse("Invalid creadentials...")


def reg_view(request):
    return render(request,'reg.htm')


def order_history(request):
    rest=restaurants.objects.all()
    return render(request,'datatable.html',{"data":rest})


@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

def chart_detail(request):
    labels=[]
    data=[]
    queryset=Sold.objects.order_by('-nosold')[:5]
    for person in queryset:
        labels.append(Sold.Dishes)
        data.append(Sold.nosold)
    return render(request,'newcharts.html',{'labels':labels,
                                            "data": data } )
