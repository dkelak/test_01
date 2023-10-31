from django.shortcuts import get_object_or_404, render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
# from django.views.decorators.csrf import csrf_exempt    
# import random

def index(request):
    latest_qusetion_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_qusetion_list' : latest_qusetion_list}
    return render(request, 'poll/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/deteil.html',{
            'question': question,
            'error_message': "you didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

"""
nextId = 4
topics = [
    {'id' : 1, 'title': '전자통신컴퓨터공학부', 'body': '전자통신컴퓨터공학부에 오신걸 환영합니다.'},
    {'id' : 2, 'title': '간호학과', 'body': '간호학과에 오신걸 환영합니다.'},
    {'id' : 3, 'title': '유아교육학과', 'body': '유아교육학과에 오신걸 환영합니다.'}
    ]

def HtML_Template(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href ="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
        <html>
        <body>
            <h1><a href ="/">Django</a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <li><a href = "/create/">create</a></li>
            <ul>
        </body>
        </html>
    '''
def index(request):
    article = '''<h2>Welcome</h2>
    안녕하세요. 장고입니다.'''
    return HttpResponse(HtML_Template(article))

@csrf_exempt
def create(request):
    global nextId    
    if request.method == 'GET':
        article = '''
            <form action = "/create/" method = "POST">
                <p><input type = "text" name = "title" placeholder = "title"></p>
                <p><textarea name = "body" placeholder = "body"></textarea name.</p>
                <p><input type = "submit"></p> 
            </form>
        '''
        return HttpResponse(HtML_Template(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append = (newTopic)
        nextId = nextId + 1
        print(request.POST)
        return HttpResponse(HtML_Template('aaa'))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2> {topic["title"]}</h2>{topic["body"]}</h2>'
    return HttpResponse(HtML_Template(article))
"""


