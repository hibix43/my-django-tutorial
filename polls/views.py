from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.db.models import F
from .models import Choice, Question

class IndexView(generic.ListView):
    # テンプレートの指定
    template_name = 'polls/index.html'
    # 描画するオブジェクトの指定
    context_object_name = 'latest_question_list'
    # クエリ
    def get_queryset(self):
        # 未来のデータは表示しない
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
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
