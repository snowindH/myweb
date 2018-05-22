#-*-coding:utf-8-*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

#create your views here.

def index(request):
    return HttpResponse('Hello world,you are at the tool index')

def homepage(request):
    template=get_template('index.html')
    posts=Post.objects.all()
    now = datetime.now()
    html=template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post != None:
            html=template.render(locals())
        return HttpResponse(html)
    except:
        return redirect('/')
def count_seq(request):
    if request.method=='POST':
        seq_a=request.POST.get('seq_a','').upper()
        seq_c=request.POST.get('seq_c','').upper()
        #获取pdb文件内容＃
        pdb=request.FILES.get('pdb','')
    seq_count=0
    seq_position=0
    seq_positions=''
    if seq_a and seq_c:
        seq_count=seq_a.count(seq_c)
        seq_position=seq_a.find(seq_c)
        while seq_position!=-1:
            seq_positions+=str(seq_position)+'|'
            seq_position = seq_a.find(seq_c,seq_position+1)
    else:
        seq_a=''
        seq_c=''
    html=render(request,'count.html',{'seq_a':seq_a,'seq_c':seq_c,'seq_count':seq_count,'seq_positions':seq_positions,'pdb':pdb,})
    return HttpResponse(html)