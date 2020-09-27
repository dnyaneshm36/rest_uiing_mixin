import json
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from django.shortcuts import get_object_or_404 
from rest_framework.generics import ListAPIView
#local file
from friend.models import Myfrienddetail
from .serializers import MyfrienddetailSerializer




from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("hello freend hello")


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView): 


    permission_classes        =[]
    authentication_classes    =[]
    serializer_class          =MyfrienddetailSerializer
    passed_id                 =None
    def get_queryset(self):
        request = self.request
        qs = Myfrienddetail.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def get_object(self):
        request         =self.request
        passed_id       =request.GET.get('id',None) or self.passed_id

        # print(request.body)
        # print(passed_id)
        # print(request.data)     
        queryset        =self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id = passed_id)
            self.check_object_permissions(request,obj)
        return obj  

    def get(self,request,*args,**kwargs):
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            #print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request, *args,**kwargs)
        return super(StatusAPIView,self).get(request,*args,**kwargs)



    def post(self,request,*args,**kwargs): 
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id        
        return self.create(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id        
        return self.update(request,*args,**kwargs)


    def patch(self,request,*args,**kwargs):
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id        
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id        
        return  self.destroy(request,*args,**kwargs)









'''

can perform all the operation crud 
if it should pass id in urls ....?id=1
else in json oject pass the id in it go update

'''
