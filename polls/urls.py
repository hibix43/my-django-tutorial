from django.urls import path
from . import views

urlpatterns = [
    # views.pyのindexメソッドをindexとする
    path('', views.index, name='index'),
]
