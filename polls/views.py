from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from .models import Choice, Question

def index(request):
    # 最新５件を取得
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # dictにして渡す
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try-exceptせずに404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # エラーメッセージを引数に表示し直し
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # F式を使うと、競合状態は発生しない
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # 成功したら結果ページへ。reverse()によりpoll/id/resultsを取得
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
