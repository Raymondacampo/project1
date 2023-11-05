from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from . import util
from markdown2 import Markdown
# from django.urls import reverse

def md_to_html(title):
    content = util.get_entry(title)
    mark = Markdown()
    if content == None:
        return None
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
            p = []
            for entry in util.list_entries():
                if t.lower() in entry.lower():
                    p.append(entry)

            return render(request, 'encyclopedia/options.html', {
            "possibilities": p
            })

def new(request):
    if request.method =='POST':
        ti, con = request.POST['page'].split(' ', 1)
        if ti not in util.list_entries():
            util.save_entry(ti, con)
            return render(request, "encyclopedia/entry.html", {
                "entry": ti, "content": md_to_html(ti)
            })
    else:
        return render(request, 'encyclopedia/new.html')

def edit(request, doc):
    if request.method =='POST':
        con = request.POST['q']
        util.save_entry(doc, con)
        return render(request, 'encyclopedia/entry.html', {
            "entry": doc, "content": md_to_html(doc)
        })
        
    return render(request, 'encyclopedia/edit.html', {
        'doc':doc, 'cont':util.get_entry(doc)
    })

    
