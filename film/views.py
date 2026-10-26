from django.shortcuts import render
from rest_framework.views import APIView
from film.permissions import ISOwner
from film.serializers import MoviesSerializer
from film.models import Movies
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.shortcuts import get_object_or_404
# Create your views here.
class MoviesListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Movies.objects.all()
        serializer_instance=MoviesSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer = MoviesSerializer(data=form_data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
class MoviesListRetrieveview(APIView):
     authentication_classes=[authentication.TokenAuthentication]
     permission_classes=[ISOwner]

     def get(self,request,pk=None):
        qs=get_object_or_404(Movies,id=pk)
        serializer_instance=MoviesSerializer(qs)
        return Response(data=serializer_instance.data)
     
     def put(self,request,pk=None):
         instance=get_object_or_404(Movies,id=pk)
         form_data=request.data
         serializer_instance=MoviesSerializer(data=form_data,instance=instance)
         if serializer_instance.is_valid(): 
             serializer_instance.save()
             return Response(serializer_instance.data)
         else:
            return Response(serializer_instance.errors)
          
     def delete(self,request,pk=None):
         instance=get_object_or_404(Movies,id=pk)
         instance.delete()
         return Response({"message": "Expense deleted successfully"})