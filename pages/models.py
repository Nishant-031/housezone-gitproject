from django.db import models

# Create your models here.

class Team(models.Model):
    first_name= models.CharField(max_length= 255)
    last_name= models.CharField(max_length= 255)
    designation= models.CharField(max_length= 255)
    image= models.ImageField(upload_to= 'photo/%Y/%m/%d/')
    facebook_link= models.URLField(max_length= 100)
    twitter_link= models.URLField(max_length= 100)
    google_plus_link= models.URLField(max_length= 100)
    created_date= models.DateTimeField(auto_now_add= True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name
