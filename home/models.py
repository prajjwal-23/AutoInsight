from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

#ContactForm
class Contact(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

#Tag
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


#Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

#Company
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='Images/upload/logo')
    category = models.ManyToManyField(Category, related_name='company')

    def __str__(self):
        return self.name
    
# Author
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

#News
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='Images/upload')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    companies = models.ManyToManyField(Company, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
