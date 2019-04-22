from django.db import models
from django.contrib.auth.models import User 

class Product(models.Model):
    title= models.CharField(default='Default Title', max_length=150)
    date = models.DateTimeField()
    body=models.TextField(default='Body of post goes here up to 500 character')
    url=models.TextField()
    image= models.ImageField(upload_to='images/')
    icon= models.ImageField(upload_to='images/',default='')
    votes_total=models.IntegerField(default=1)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        str(self.body)
        return self.body[:300]

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
    

