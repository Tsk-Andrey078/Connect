from pyexpat import model
from django.db import models

# Create your models here.
class chats(models.Model):
    slug = models.SlugField()
    person_name = models.CharField(max_length=255)
    last_message = models.CharField(max_length=255)

    def __str__(self):
        return self.person_name

    def get_data(self):
        return (self.person_name, self.last_message)

class message(models.Model):
    chat = models.ForeignKey(chats,related_name='message', on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    date = models.DateField()
    author_name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.message

    def get_adress(self):
        return f'{self.chat.slug}/{self.slug}/'

    def get_message(self):
        return (self.message, self.chat, self.date, self.author_name, self.slug)

class account(models.Model):
    slug = models.SlugField()
    name = models.TextField()
    chats = models.TextField()

    def __str__(self):
        return self.name