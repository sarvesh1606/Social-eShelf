from django.shortcuts import render
from django.http import JsonResponse
import requests , json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend 



from .serializers import EbookSerializer

from ebook.models import Ebook




# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls= {
        'Ebook List': '/ebooklist/' ,
        'Specific Ebook View': '/ebookspecific/<ebook id>/',
        'Create Ebook':'/ebookcreate/',
        'Update Ebook':'/ebookupdate/<ebook id>/',
        'Delete Ebook':'/ebookdelete/<ebook id>/',
    
    
    }

#    return JsonResponse("API base point" , safe=False)
    return Response(api_urls)

@api_view(['GET'])
def ebookList(request):
    
    ebooks= Ebook.objects.all()
    serializer= EbookSerializer(ebooks , many= True)
    return Response(serializer.data)



@api_view(['GET'])
def ebookSpecific(request , sk):
    
    ebooks= Ebook.objects.get(id=sk)
    serializer= EbookSerializer(ebooks , many= False)
    return Response(serializer.data)

@api_view(['POST'])
def ebookCreate(request):
    
    serializer= EbookSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def ebookUpdate(request , sk):
    
    ebooks= Ebook.objects.get(id=sk)
    serializer= EbookSerializer( instance=ebooks , data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def ebookDelete(request , sk):
    
    ebook= Ebook.objects.get(id=sk)
    ebook.delete()

    return Response("Ebook deletion successful")



class searchApi(generics.ListAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ['title']
#    filter_backends= [DjangoFilterBackend]
#    filterset_fields = ['title', 'completed']



