from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from film.views import MoviesListCreateView,MoviesListRetrieveview
urlpatterns=[
     path('admin/token/',ObtainAuthToken.as_view()),
     path('movie/',MoviesListCreateView.as_view()),
     path('movie/<int:pk>/',MoviesListRetrieveview.as_view()),
]

