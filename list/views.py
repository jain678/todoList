from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TodoView(APIView):
    
    def get_object(self, pk):
        try:
            return Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):           
        if pk is None:                                          # 
            task = Tasks.objects.all()
            serializer = TasksSerializer(task,many=True)
        else:
            task = self.get_object(pk)
            serializer = TasksSerializer(task)
        return Response(serializer.data)

    def post(self, request, format=None):
       
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class MarkdoneAPIView(APIView):
   
    def get_object(self, pk):
        try:
            return Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        task = self.get_object(pk)
        print(task)
        task.mark_as_done()
        task = self.get_object(pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data)
