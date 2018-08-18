from django.db import models

class Question(models.Model):
    # 質問事項（テキストデータ）
    question_text = models.CharField(max_length=200)
    # 公開日（日時データ）
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # ChoiseをQuestionに関連づける
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 選択肢
    choice_text = models.CharField(max_length=200)
    # 投票数（整数データ）
    votes = models.IntegerField(default=0)

