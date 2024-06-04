from django.db import models
from datetime import datetime
# Create your models here.
class post(models.Model) :
    title = models.CharField(max_length=100)  # Correct
    body  =models.TextField()
    published_date = models.DateTimeField(default = datetime.now,blank = True)  # Correct

