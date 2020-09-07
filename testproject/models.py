from django.db import models

class Examples(models.Model):   
    name = models.CharField(max_length=100)
    class Meta:
        db_table = "example"
