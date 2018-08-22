from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    # 余分に表示
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Adim編集フォームの並び順を指定
    # fields:フォームをまとめて見出しとともに表示
    # classes: collapseにて折りたたみ表示にする
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    # XXInlineによりXX表示(ex:Stack>>列表示)
    inlines = [ChoiceInline]

# Modelごとに引数で渡す
admin.site.register(Question, QuestionAdmin)
