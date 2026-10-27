from django.urls import path
from review.views import ReviewListCreateView,ReviewRetrieveUpdateDeleteView
urlpatterns=[
    path('song/<int:pk>/review/',ReviewListCreateView.as_view()),
    path('review/<int:pk>',ReviewRetrieveUpdateDeleteView.as_view())

]