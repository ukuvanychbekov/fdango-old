from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()

#
# def index(request):
#     questions = Question.objects.all()
#     context = {
#         'latest_question_list' : questions,
#     }
#     return render(request, 'index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     context = {'question': question}
#     return render(request, 'detail.html', context)

class ResultView(generic.DetailView):
    model = Question
    template_name = 'result.html'

# def result(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     context = {'question': question}
#     return render(request, 'result.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice = question.choice_set.get(id=request.POST['choice'])
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('result', args=(question.id, )))


