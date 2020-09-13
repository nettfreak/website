from django .http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'hello':'taha'})

def homepage(request):
    return HttpResponse('homepage')

def count(request):
    text=request.GET.get('text')
    wordlist=text.split()
    worddic={}
    
    for word in wordlist:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1

    sortword=sorted(worddic.items(),key=operator.itemgetter(1),reverse=True)        

    return render(request,'count.html',{'text':text,'count':len(wordlist),'sortword':worddic.items()})