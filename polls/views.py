from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.template import loader
from .models import Question, Choice, Room, Hupu
from django.urls import reverse
from django.views import generic
from django.core import serializers
from rest_framework import generics
from .serializers import RoomSerializers, QuestionSerializers, HupuSerializers

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

def savehupu(request, page=1):
    import requests
    from polls.models import Hupu

    url = 'https://soccer.hupu.com/api/v1/fifa'
    r = requests.get(url, params={'p': page}).json()
    data = r.get('data')
    for j in data:
        c = j.get('content')
        t = j.get('title')
        news = Hupu(hupu_title = t, hupu_content = c)
        news.save()
    return JsonResponse({'data':data})

class HupuView(generics.ListAPIView):
    queryset = Hupu.objects.all()
    serializer_class = HupuSerializers

class QuestionView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five published question.'''
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

# def detail(request, id):
#     q = get_object_or_404(Question, pk=id)
#     return render(request, 'polls/detail.html', {'question':q})

# def results(request, id):
#     question = get_object_or_404(Question, pk=id)
#     return render(request, 'polls/results.html', {'question':question})

def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_massage': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def json(request, id):
    q = Question.objects.get(id=id)
    # questiontext = q.question_text
    c = q.choice_set.all()
    serialized_object = serializers.serialize('json', c)
    return JsonResponse(
        {
            'id': id,
            'text': q.question_text,
            'choice': serialized_object,
        }
    )

# def helloworld(request):
#     # print(request)
#     return HttpResponse('Hello world')
