from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question

def index(request):
    # 最新５件を取得
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # dictにして渡す
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 例外処理にて404Error処理
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question_id})

def results(request, question_id):
    response = "You're looking at question %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You',re voting on question %s." % question_id)
