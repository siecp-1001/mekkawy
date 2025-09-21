from django.db import models
class Link(models.Model):
    url = models.URLField()
    label = models.CharField(max_length=255, blank=True, null=True)  # optional name
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label or self.url

class Transportation(models.Model):
    title = models.CharField(max_length=255)
    cartype=models.CharField(max_length=255)
    priceperday=models.CharField(max_length=300)
    pricepermonth=models.CharField(max_length=300)
    description = models.TextField()
   
    links = models.ManyToManyField(Link, blank=True)



class HomePage(models.Model):
    title = models.CharField(max_length=255)
    banner = models.URLField(blank=True, null=True)
    content = models.TextField()
    links = models.ManyToManyField(Link, blank=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    links = models.ManyToManyField(Link, blank=True)

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    links = models.ManyToManyField(Link, blank=True)

class Career(models.Model):
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    links = models.ManyToManyField(Link, blank=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    links = models.ManyToManyField(Link, blank=True)

class Portfolio(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    links = models.ManyToManyField(Link, blank=True)

class TravelTicket(models.Model):
    destination = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    links = models.ManyToManyField(Link, blank=True)

class HajjOmrah(models.Model):
    package_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    links = models.ManyToManyField(Link, blank=True)

class Retail(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    links = models.ManyToManyField(Link, blank=True)

class Travelpackages(models.Model):
    product_name = models.CharField(max_length=500)
    description = models.TextField()
    image = models.CharField(max_length=450)
    links = models.ManyToManyField(Link, blank=True)
