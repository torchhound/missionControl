from django.http import HttpResponse
from django.template import Context, loader

def livingRoom(request):
    template = loader.get_template("livingRoom.html")
    return HttpResponse(template.render())

def kittyCorner(request):
    template = loader.get_template("kittyCorner.html")
    return HttpResponse(template.render())
	
def bathroom(request):
    template = loader.get_template("bathroom.html")
    return HttpResponse(template.render())
