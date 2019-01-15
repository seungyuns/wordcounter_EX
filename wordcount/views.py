from django.shortcuts import render
from collections import defaultdict

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def result(request):
    
    d=defaultdict()
    d=defaultdict(lambda:0)
    
    text = request.GET['fulltext']
    words = text.split(" ")
    for i in words:
        d[i] = d[i]+1

    return render(request, 'result.html', { 'full' : text, 'total' : len(words), 'num_c':d.items()})