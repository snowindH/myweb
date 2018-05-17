# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
#def index(request):
#    return HttpResponse("Hello,world,You're at the tool index.")
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    return HttpResponse(post_lists)
