from django.http import HttpResponse
from django.template import Context, loader
import requests

def livingRoom(request):
	if request.method == "GET":
		template = loader.get_template("livingRoom.html")
		return HttpResponse(template.render())
	elif request.POST.get("on", False):
		requests.post("http://localhost:5000/livingroom", data = {"on":True})
	elif request.POST.get("off", False):
		requests.post("http://localhost:5000/livingroom", data = {"off":True})
	elif request.POST.get("dim", False):
		requests.post("http://localhost:5000/livingroom", data = {"dim":True})
	elif request.POST.get("night", False):
		requests.post("http://localhost:5000/livingroom", data = {"night":True})
	else:
		return HttpRequest(status=400)

def kittyCorner(request): #set action= separate endpoints or this function?
	if request.method == "GET":
		template = loader.get_template("kittyCorner.html")
		return HttpResponse(template.render())
	elif request.POST.get("on", False):
		requests.post("http://localhost:5000/kittycorner", data = {"on":True})
	elif request.POST.get("off", False):
		requests.post("http://localhost:5000/kittycorner", data = {"off":True})
	elif request.POST.get("dim", False):
		requests.post("http://localhost:5000/kittycorner", data = {"dim":True})
	elif request.POST.get("night", False):
		requests.post("http://localhost:5000/kittycorner", data = {"night":True})
	else:
		return HttpRequest(status=400)
		
def kcon(request):
	print("kcon")
	requests.post("http://localhost:5000/kittycorner", data = {"on":True})

def bathroom(request):
    template = loader.get_template("bathroom.html")
    return HttpResponse(template.render())
