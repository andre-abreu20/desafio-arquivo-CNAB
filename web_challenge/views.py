from django.http import HttpResponse
from django.shortcuts import render

posts = [{
    "author": "Andre",
    "title": "rich",
    "content": "none",
},
{
    "author": "Cesar",
    "title": "rich",
    "content": "yes?",
}]


def index(request):
    context= {
        "posts": posts
    }
    return render(request, "web_challenge/index.html", context)

def doc(request):
    return render(request, "web_challenge/doc.html", {"title": "Documentation"})
