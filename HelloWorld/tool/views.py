#-*-coding:utf-8-*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
import os
from . import run
#create your views here.
#global k,r,rmsd,pdb

def index(request):
    return HttpResponse('Hello world,you are at the tool index')

def homepage(request):
    template=get_template('home.html')
    html=template.render()
    return HttpResponse(html)
def result(request):
    template=get_template('result.html')

    html=template.render(locals())
    
    return HttpResponse(html)
def showpost(request):
    #global k,r,rmsd,pdb
    if request.method=='POST':
        template=get_template('tool.html')
        r=request.POST.get('r','')
        rmsd=request.POST.get('rmsd','')
        k=request.POST.get('k','')
        pdb=request.FILES.get('pdb','')
        #在数据库中插入参数
        print pdb
        path = os.getcwd()
        p = './static/files/'
        print path
        os.system('touch ' + p + 'data.pdb')
        destination = open(os.path.join(p + 'data.pdb'),'wb+')
        for chunk in pdb.chunks():
            destination.write(chunk)
        destination.close()
        pdbname=pdb.name
        html=render(request,'tool.html',{"r":r, "k":k, "rmsd":rmsd, "pdbname":pdb.name})
        s = run.pdb_deal()
        s.get_dimer()
        return HttpResponse(html)
    template=get_template('tool.html')
    html=template.render()
    return HttpResponse(html)
