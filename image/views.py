from django.shortcuts import redirect, render
from helpers import get_image_size
from .models import ImageObject, ImageTask, Category

# Create your views here.
def complete_task(request):
    tasks = ImageTask.objects.filter().order_by("-priority")
    categories = Category.objects.filter(image_task=tasks[1])
    return render(request, "image/index.html", {
        "task": tasks[1],
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
