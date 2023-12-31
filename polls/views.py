from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# # template = loader.get_template("polls/index.html")
# # context = {
# #     "latest_question_list": latest_question_list,
# # }
# # return HttpResponse(template.render(context, request)) 
# # above no longer needed with the render() function
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context) 
# #render() function takes the request object as its first argument, 
# #a template name as its second argument and a dictionary as its optional 
# #third argument. It returns an HttpResponse object of the given template 
# #rendered with the given context.

# def detail(request, question_id):
#     # try: #deals with the 404 error if it occurs
#     #         question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #         raise Http404("Question does not exist") 
#     # The view raises the Http404 exception if a question with the 
#     # requested ID doesn’t exist.
#     # return render(request, "polls/detail.html", {"question": question})
#     question = get_object_or_404(Question, pk=question_id) 
#     #takes model as first argu and a number of keyword argus, 
#     # then passes to get() funtion
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
# # request.POST is a dictionary-like object that lets you access submitted data by key name. 
# # In this case, request.POST['choice'] returns the ID of the selected choice, as a string.
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# using the generic views given by django we can resuce the amount of code we have
# everything above can be condensed into this:     
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # """Return the last five published questions."""
        # return Question.objects.order_by("-pub_date")[:5]]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
# same as above, no changes needed.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
# request.POST is a dictionary-like object that lets you access submitted data by key name. 
# In this case, request.POST['choice'] returns the ID of the selected choice, as a string.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))    