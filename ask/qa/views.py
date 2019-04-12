from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound 
from qa.models import Question, Answer
from django.core.paginator import Paginator, InvalidPage
from django.urls import reverse

def paginator_call(request, obj_list):
    limit = 10 #request.GET.get('limit', 10)
    paginator = Paginator(obj_list, limit)
    try:
        page_num = int(request.GET.get('page', 1))
    except (ValueError, TypeError):
        page_num = 1
    try:
        page = paginator.page(page_num)
    except InvalidPage:
        not_found(request)    
    return (paginator, page)

def new_questions_list(request):
    questions = Question.objects.new()
    paginator, page = paginator_call(request,questions)
    paginator.baseurl = reverse('qa_new') + '?page='
    return render(request, 'questions_list.html', 
                    {'questions' : page.object_list,
                    'paginator' : paginator,
                    'page' : page,
                    'page_name' : 'New'
                    })

def popular_questions_list(request):
    questions = Question.objects.popular()
    paginator, page = paginator_call(request,questions)
    paginator.baseurl = reverse('qa_popular') + '?page='
    return render(request, 'questions_list.html', 
                    {'questions' : page.object_list,
                    'paginator' : paginator,
                    'page' : page,
                    'page_name' : 'Popular'
                    })

def question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'question.html', 
                    {'question' : question, 
                    'answers' : question.answer_set.all()})


def test(request, *args, **kwargs):
    id = kwargs.get('id', '')
    resp = 'OK ' + str(id)
    return HttpResponse(resp) 

def not_found(request):
    return HttpResponseNotFound("Not Found!")
