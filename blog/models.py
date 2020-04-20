from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    lead = models.TextField(max_length=400)
    content = models.TextField(max_length=1200)
    author = models.CharField(max_length=50)
    create_date = models.DateField()
    publish_date = models.DateField()

    def summary(self):
        return self.content[:400]

    def publish_date_different(self):
        return self.publish_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title