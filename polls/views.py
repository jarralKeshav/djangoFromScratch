from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    # return HttpResponse("Hello Polls Index.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list}
    return render(request, "polls/index.html", context)

    # return HttpResponse(template.render(context,request))


    # output = ",".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Your're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking ar the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




# # Create your views here.
