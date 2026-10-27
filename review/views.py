from django.shortcuts import render
from rest_framework.views import APIView
from film.models import Movies
from review.models import Reviews
from rest_framework import authentication,permissions
from review.serializers import ReviewSerializers
from review.permissions import IsOwner
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
# Create your views here.

class ReviewListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):
        qs=Movies.objects.get(id=pk)
        form_data=request.data
        serializer_instance=ReviewSerializers(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(movie=qs,owner=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class ReviewRetrieveUpdateDeleteView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializers