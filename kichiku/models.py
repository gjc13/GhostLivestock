from django.db import models


# Create your models here.
class Audio(models.Model):
    text = models.CharField(max_length=100)
    file = models.FileField(upload_to='./Audio/')
    pub_date = models.DateField('date published')

    def __unicode__(self):
        return self.text