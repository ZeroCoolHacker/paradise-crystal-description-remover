from django.db import models

# Create your models here.
class ProductDescriptionChange(models.Model):

    handle = models.CharField(max_length=50)
    description_changed = models.BooleanField(default=False)
    date_tried = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.handle} - {self.description_changed} - {self.date_tried}'