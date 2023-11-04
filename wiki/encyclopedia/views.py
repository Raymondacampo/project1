from django.shortcuts import render
from django.http import Http404
from . import util
from markdown2 import Markdown

def md_to_html(title):
    content = util.get_entry(title)
    mark = Markdown()
    if content == None:
        return Null
    else:
        return mark.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    if name in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": name, "content": md_to_html(name)
        })

def search(request):
    if request.method == 'POST':
        t = request.POST['q']
        search_content = md_to_html(t)
        if search_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "entry": t, "content": search_content
            })
        else:
            raise Http404