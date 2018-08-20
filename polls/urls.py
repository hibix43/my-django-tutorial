from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex /polls/
    path('', views.index, name='index'),
    # ex /polls/1 name引数指定により{% url detail (引数)が可能 %}
    path('<int:question_id>/', views.detail, name='detail'),
    # ex /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
] 
