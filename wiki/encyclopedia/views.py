from django.shortcuts import render

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    if name in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": name, "content": util.get_entry(name)
        })
