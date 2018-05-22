#-*- coding:utf-8-*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

#Create your views here.

def index(request):
    return HttpResponse('Hello world,you are at the tool index')

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
