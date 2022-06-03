import json
from tkinter import Y
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render
from helpers import get_image_size
from .models import ImageObject, ImageTask, Category
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def complete_task(request):
    tasks = ImageTask.objects.filter(is_complete=False).order_by("-priority")
    categories = Category.objects.filter(image_task=tasks[0])
    return render(request, "image/index.html", {
        "task": tasks[0],
        "categories": categories
    })

def add_task(request):
    if request.method == "POST":
        url = request.POST["url"]
        w, h = get_image_size(url)
        
        priority = request.POST["priority"]

        task = ImageTask.objects.create(priority=priority, image_url=url, width=w, height=h)
        
        categories = request.POST["categories"].split(", ")
        for c in categories:
            Category.objects.create(image_task=task, name=c)
        
        return redirect("/image/add")
    else:
        return render(request, "image/add.html")

@csrf_exempt
def submit_task(request):
    if request.method == "POST":
        json_data = json.loads(request.body) 
        task_id = json_data["task_id"]
        task = ImageTask.objects.get(id=int(task_id))
        object_total = int(json_data["object_total"])
        for obj_index in range(object_total):
            x = json_data[f"obj" + str(obj_index) + "-x"]
            y = json_data[f"obj" + str(obj_index) + "-y"]
            w = json_data[f"obj" + str(obj_index) + "-w"]
            h = json_data[f"obj" + str(obj_index) + "-h"]
            category = json_data[f"obj" + str(obj_index) + "-category"]
            category = Category.objects.get(name=category, image_task=task)
            ImageObject.objects.create(image_task=task, x=int(x), y=int(y), w=int(w), h=int(h), category=category)
        task.is_complete = True
        task.save()
        return HttpResponse("Task Completed")
    else:
        return HttpResponseNotFound("404 Not Found")

def submit_task_view(request):
    return render(request, "image/submitted.html")
