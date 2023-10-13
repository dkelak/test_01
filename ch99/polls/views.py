from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id' : 1, 'title': '전자통신컴퓨터공학부', 'body': '전자통신컴퓨터공학부에 오신걸 환영합니다.'},
    {'id' : 2, 'title': '간호학과', 'body': '간호학과에 오신걸 환영합니다.'},
    {'id' : 3, 'title': '유아교육학과', 'body': '유아교육학과에 오신걸 환영합니다.'},
    {'id' : 4, 'title': '기계자동차공학부', 'body': '기계자동차공학부에 오신걸 환영합니다.'},
    {'id' : 5, 'title': '물리치료학과', 'body': '물리치료학과에 오신걸 환영합니다.'},
    {'id' : 6, 'title': '특수건설기계학과', 'body': '특수건설기계학과에 오신걸 환영합니다.'}
    ]

def HtML_Template(articletag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href ="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
        <html>
        <body>
            <h1>Django</h1>
            <ol>
                {ol}
            </ol>
            {articletag}
        </body>
        </html>
    '''
def index(request):
    articletag = '''<h2>Welcome</h2>
    안녕하세요. 장고입니다.'''
    return HttpResponse(HtML_Template(articletag))

def creat(request):
    return HttpResponse('안녕하세요 creat 홈페이지에 오신걸 환영합니다')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2> {topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HtML_Template(article))