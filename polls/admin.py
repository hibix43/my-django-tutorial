from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    # Adim編集フォームの並び順を指定
    # フォームをまとめて見出しとともに表示
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]

# Modelごとに引数で渡す
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
