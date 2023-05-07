from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_link = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=2500)


    # Add this when I add the pillow dependency
    # project_screenshot = models.ImageField(upload_to="images/", default='../images/missing_image.jpg')