from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    # path('news/', views.news, name='news'),
    path('news/', PostList.as_view(), name='news'),
    path('news/<int:pk>', PostDetails.as_view(), name='unit_of_news'),
]
