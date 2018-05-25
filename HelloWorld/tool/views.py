#-*-coding:utf-8-*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
import os
#create your views here.

def index(request):
    return HttpResponse('Hello world,you are at the tool index')

def homepage(request):
    template=get_template('home.html')
    html=template.render()
    return HttpResponse(html)
def result(request):
    template=get_template('result.html')
    html=template.render()
    return HttpResponse(html)
def showpost(request):
    if request.method=='POST':
        template=get_template('tool.html')
        r=request.POST.get('r','')
        rmsd=request.POST.get('rmsd','')
        k=request.POST.get('k','')
        pdb=request.FILES.get('pdb','')
        print pdb
        os.system('touch /home/hxf/examples/my_python/Django/myweb/HelloWorld/static/files/%s'%(pdb.name))
        destination = open(os.path.join('/home/hxf/examples/my_python/Django/myweb/HelloWorld/static/files/',pdb.name),'wb+')
        for chunk in pdb.chunks():
            destination.write(chunk)
        destination.close()
        pdbname=pdb.name

        html=render(request,'tool.html',locals())
        return HttpResponse(html)
    template=get_template('tool.html')
    html=template.render()
    return HttpResponse(html)

def count_seq(request):
    if request.method=='POST':
        seq_a=request.POST.get('seq_a','').upper()
        seq_c=request.POST.get('seq_c','').upper()
        #获取pdb文件内容＃
        pdb=request.FILES.get('pdb','')
        os.system('touch /home/hxf/examples/my_python/Django/myweb/HelloWorld/static/files/%s'%(pdb.name))
        destination = open(os.path.join('/home/hxf/examples/my_python/Django/myweb/HelloWorld/static/files/',pdb.name),'wb+')
        for chunk in pdb.chunks():
            destination.write(chunk)
        destination.close()
    else:
        seq_a=''
        seq_c=''
        pdb =''
    seq_count=0
    seq_position=0
    seq_positions=''
    
    if seq_a and seq_c:
        seq_count=seq_a.count(seq_c)
        seq_position=seq_a.find(seq_c)
        while seq_position!=-1:
            seq_positions+=str(seq_position)+'|'
            seq_position = seq_a.find(seq_c,seq_position+1)

    html=render(request,'count.html',{'seq_a':seq_a,'seq_c':seq_c,'seq_count':seq_count,'seq_positions':seq_positions,'pdb':pdb,})
    return HttpResponse(html)