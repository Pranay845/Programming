# I have created this file - pranay
from django.http import HttpResponse
from django.shortcuts import render


# function for showing html template in home page

def index(request):
    # render takes two arguments
    # 1.request
    # 2.the template name to search
    return render(request, 'Home.html')


def analyze(request):
    # Get the text
    global params
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analyzed = analyzed + char

            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if numberremover == "on":
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    # check if all checkboxes are off
    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numberremover != "on":
        params = {'purpose': 'not selected any operation', 'analyzed_text': f'select a operation for your text\n\nyour text:{djtext}'}
        return render(request, 'Analyze.html', params)
    # check if all checkboxes are on
    if removepunc == "on" and newlineremover == "on" and extraspaceremover == "on" and fullcaps == "on" and numberremover == "on":
        params = {'purpose': 'Use Only one operation', 'analyzed_text': f'Can t analyze\n\nyour text:{djtext.lower()}'}
        return render(request, 'Analyze.html', params)

    return render(request, 'Analyze.html', params)


# function for about page
def about(request):
    return render(request, 'About.html')

