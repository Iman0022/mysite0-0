from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# Choices are edited in the Question admin page
# Provide fields for 3 choiced by dafault

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"] 
    # # makes it so the pub date shows before the question text

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
# splits the form into feildsets: question text above separated from the rest
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"] #adds a filter to sort by date
    search_fields = ["question_text"] #adds a search box at the top of the change list

admin.site.register(Question, QuestionAdmin)
# idk why but page wont load