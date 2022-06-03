from django.db import models

# Create your models here.
class ImageTask(models.Model):
    priority = models.IntegerField() # 1: Really urgent, 2: Urgent, 3: Normal
    image_url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    is_complete = models.BooleanField(default=False)

class Category(models.Model):
    image_task = models.ForeignKey(ImageTask, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class ImageObject(models.Model):
    image_task = models.ForeignKey(ImageTask, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
