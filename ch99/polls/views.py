from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt    
import random

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
