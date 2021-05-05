# Developer created file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    para = None
    djtext = request.POST.get('text', 'Dafault')
    checkbox1 = request.POST.get('removepunc', 'off')
    checkbox2 = request.POST.get('uppercase', 'off')
    checkbox3 = request.POST.get('extraspaceremover', 'off')
    checkbox4 = request.POST.get('newlineremover', 'off')

    if checkbox1 == 'on':
        # logic to remove punctuations
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        para = {'analyzed_text': analyzed}
        djtext = analyzed

    if checkbox2 == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        para = {'analyzed_text': analyzed}
        djtext = analyzed

    if checkbox3 == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        para = {'analyzed_text': analyzed}
        djtext = analyzed

    if checkbox4 == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        para = {'analyzed_text': analyzed}

    if checkbox1 == 'off' and checkbox2 == 'off' and checkbox3 == 'off' and checkbox4 == 'off':
        # return HttpResponse("Error")
        para = {'analyzed_text': 'Error'}

    return render(request, 'analyze.html', para)
