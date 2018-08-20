from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    # 最新５件を取得
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # dictにして渡す
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at question %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You',re voting on question %s." % question_id)
