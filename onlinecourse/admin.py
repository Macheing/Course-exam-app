from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# administrative views.
# Register QuestionInline and ChoiceInline classes here.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 4

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionInline(admin.StackedInline):
    '''Stack questions'''
    model = Question
    extra = 4

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date','total_enrollment','users']
    search_fields = ['name', 'description']


class QuestionAdmin(admin.ModelAdmin):
    '''Dispalys list of question admin view.'''
    # stack choices below each question
    inlines = [ChoiceInline]
    # display each question, pub_date and published status in one line.
    list_display = ['text']
    # filter questions based on published dates.
    search_fields = ['text']

# Register Question and Choice models here
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
