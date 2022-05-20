# This file is created by : Sparsh
from re import A
from ssl import Purpose


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
def index(request):
    return render(request,'index.html')
def testing(request):
    
    ans=0
    n1=0
    n2=0
    try:
        n1=int(request.POST.get('val1'))
        n2=int(request.POST.get('val2'))
        ans=n1+n2
    except:
        pass
    data={
        'title':'Testing',
        'heading':'Welcome to testing page',
        'lang': ['python','java','c','c++','php'],
        'student':[{'name':'abc','phone':123},{'name':'def','phone':456}],
        'ans':ans,
        'n1':n1,
        'n2':n2
    }
    # return redirect('/')
    return render(request,'testing.html',data)

def analyze(request):
    djtext=request.POST.get("text",'dafault')
    removepunc=request.POST.get("removepunc",'off')
    fullcaps=request.POST.get("fullcaps",'off')
    newlineremove=request.POST.get("newlineremove",'off')
    extraspaceremover=request.POST.get("extraspaceremover",'off')
    charcount=request.POST.get("charcount",'off')
    purp=''
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        purp='Remove Punctuations'
        djtext=analyzed

    if fullcaps=='on':
        analyzed=djtext.upper()
        djtext=analyzed
        if purp:
            purp+=' | '
        purp+='Changed to UPPER CASE'

    if newlineremove=='on':
        analyzed=''
        for i in djtext:
            if i!='\n' and i!='\r':
                analyzed+=i
        djtext=analyzed
        if purp:
            purp+=' | '
        purp+='New Line Removed'

    if extraspaceremover=='on':
        analyzed=''
        for index,i in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed+=i
        djtext=analyzed
        if purp:
            purp+=' | '
        purp+='Extra Space Removed'

    if removepunc!='on' and fullcaps!='on' and newlineremove!='on' and extraspaceremover!='on' and charcount!='on':
        return HttpResponse('Error')
    params={'purpose':purp,'analyzed_text':analyzed}
    return render(request,'analyze.html',params)