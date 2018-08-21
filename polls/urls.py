from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex /polls/
    # 汎用ビューの利用
    path('', views.IndexView.as_view(), name='index'),
    # ex /polls/1 name引数指定により{% url detail (引数)が可能 %}
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex /polls/1/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
] 
