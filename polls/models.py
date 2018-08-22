import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    # 質問事項（テキストデータ）
    # 変数名がデータベースの列名となる
    question_text = models.CharField(max_length=200)
    # 公開日（日時データ）
    # 第一引数がデータベースの列名となる
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # Demo
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    # ChoiseをQuestionに関連づける
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 選択肢
    choice_text = models.CharField(max_length=200)
    # 投票数（整数データ）
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
