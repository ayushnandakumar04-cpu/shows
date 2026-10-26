from django.shortcuts import render
from rest_framework.views import APIView
from music.models import Song
from music.serializers import SongSerializers
from rest_framework.response import Response
from film.models import Movies
from rest_framework.generics import DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import authentication,permissions
# Create your views here.
class SongCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):
        qs=Movies.objects.get(id=pk)
        form_data=request.data
        serializer_instance=SongSerializers(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(movies=qs,created_by=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class SongRetrieveUpdateDeleteView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    queryset=Song.objects.all()
    serializer_class=SongSerializers
