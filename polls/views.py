from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404, get_object_or_404, render

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
# template = loader.get_template("polls/index.html")
# context = {
#     "latest_question_list": latest_question_list,
# }
# return HttpResponse(template.render(context, request)) 
# above no longer needed with the render() function
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context) 
#render() function takes the request object as its first argument, 
#a template name as its second argument and a dictionary as its optional 
#third argument. It returns an HttpResponse object of the given template 
#rendered with the given context.

def detail(request, question_id):
    # try: #deals with the 404 error if it occurs
    #         question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #         raise Http404("Question does not exist") 
    # The view raises the Http404 exception if a question with the 
    # requested ID doesn’t exist.
    # return render(request, "polls/detail.html", {"question": question})
    question = get_object_or_404(Question, pk=question_id) 
    #takes model as first argu and a number of keyword argus, 
    # then passes to get() funtion
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)