from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    # Sets 'latest_question_list' to a Question list ordered
    # by reverse order of publish date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Creates a dictionary linking 'latest_question_list' string to the
    # list of the same name (allowing easy access)
    context = {'latest_question_list': latest_question_list}
    # Uses render() to return the index template in 'context'
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)
