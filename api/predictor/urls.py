
from django.urls import path
from .import views


urlpatterns = [
  path('',views.home,name="home"),
  path('predictor/result',views.result,name="result"),
]
