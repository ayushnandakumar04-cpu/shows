from django.urls import path
from music.views import SongCreateView,SongRetrieveUpdateDeleteView
urlpatterns=[
    path('movie/<int:pk>/song/',SongCreateView.as_view()),
    path('movie/<int:pk>/song/<int:pk>',SongRetrieveUpdateDeleteView.as_view())

]