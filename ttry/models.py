from django.db import models
from googletrans import Translator

translator = Translator()


class Link(models.Model):
    url = models.URLField()
    label = models.CharField(max_length=255, blank=True, null=True)  # optional name
    label_ar = models.CharField(max_length=255, blank=True, null=True)  # Arabic label
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.label_ar and self.label:
            self.label_ar = translator.translate(self.label, dest='ar').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label or self.url


class Transportation(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, blank=True, null=True)

    # Car booking fields
    pickup_location = models.CharField(max_length=255)  
    pickup_location_ar = models.CharField(max_length=255, blank=True, null=True)

    pickup_date = models.DateField()
    return_date = models.DateField()

    cartype = models.CharField(max_length=255)
    cartype_ar = models.CharField(max_length=255, blank=True, null=True)

    priceperday = models.CharField(max_length=300)
    priceperday_ar = models.CharField(max_length=300, blank=True, null=True)

    pricepermonth = models.CharField(max_length=300)
    pricepermonth_ar = models.CharField(max_length=300, blank=True, null=True)

    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)

    links = models.ManyToManyField(Link, blank=True)

    def __str__(self):
        return self.title



class HomePage(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    banner = models.URLField(blank=True, null=True)
    content = models.TextField()
    content_ar = models.TextField(blank=True, null=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.title_ar and self.title:
            self.title_ar = translator.translate(self.title, dest='ar').text
        if not self.content_ar and self.content:
            self.content_ar = translator.translate(self.content, dest='ar').text
        super().save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    content_ar = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.title_ar and self.title:
            self.title_ar = translator.translate(self.title, dest='ar').text
        if not self.content_ar and self.content:
            self.content_ar = translator.translate(self.content, dest='ar').text
        super().save(*args, **kwargs)


class Video(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.title_ar and self.title:
            self.title_ar = translator.translate(self.title, dest='ar').text
        if not self.description_ar and self.description:
            self.description_ar = translator.translate(self.description, dest='ar').text
        super().save(*args, **kwargs)


class Career(models.Model):
    job_title = models.CharField(max_length=255)
    job_title_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)
    requirements = models.TextField()
    requirements_ar = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.job_title_ar and self.job_title:
            self.job_title_ar = translator.translate(self.job_title, dest='ar').text
        if not self.description_ar and self.description:
            self.description_ar = translator.translate(self.description, dest='ar').text
        if not self.requirements_ar and self.requirements:
            self.requirements_ar = translator.translate(self.requirements, dest='ar').text
        super().save(*args, **kwargs)


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    message_ar = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.name_ar and self.name:
            self.name_ar = translator.translate(self.name, dest='ar').text
        if not self.message_ar and self.message:
            self.message_ar = translator.translate(self.message, dest='ar').text
        super().save(*args, **kwargs)


class Portfolio(models.Model):
    project_name = models.CharField(max_length=255)
    project_name_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.project_name_ar and self.project_name:
            self.project_name_ar = translator.translate(self.project_name, dest='ar').text
        if not self.description_ar and self.description:
            self.description_ar = translator.translate(self.description, dest='ar').text
        super().save(*args, **kwargs)


class TravelTicket(models.Model):
    destination = models.CharField(max_length=255)
    destination_ar = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.destination_ar and self.destination:
            self.destination_ar = translator.translate(self.destination, dest='ar').text
        super().save(*args, **kwargs)


class HajjOmrah(models.Model):
    package_name = models.CharField(max_length=255)
    package_name_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.package_name_ar and self.package_name:
            self.package_name_ar = translator.translate(self.package_name, dest='ar').text
        if not self.description_ar and self.description:
            self.description_ar = translator.translate(self.description, dest='ar').text
        super().save(*args, **kwargs)


class Retail(models.Model):
    product_name = models.CharField(max_length=255)
    product_name_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.product_name_ar and self.product_name:
            self.product_name_ar = translator.translate(self.product_name, dest='ar').text
        if not self.description_ar and self.description:
            self.description_ar = translator.translate(self.description, dest='ar').text
        super().save(*args, **kwargs)


class Travelpackages(models.Model):
    product_name = models.CharField(max_length=500)
    product_name_ar = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=450)
    links = models.ManyToManyField(Link, blank=True)

    def save(self, *args, **kwargs):
        if not self.product_name_ar and self.product_name:
            self.product_name_ar = translator.translate(self.product_name, dest='ar').text
        if not self.description_ar and self.description:
            self.description_ar = translator.translate(self.description, dest='ar').text
        super().save(*args, **kwargs)




translator = Translator()

class FlightSearch(models.Model):
    from_city = models.CharField(max_length=255)
    from_city_ar = models.CharField(max_length=255, blank=True, null=True)

    to_city = models.CharField(max_length=255)
    to_city_ar = models.CharField(max_length=255, blank=True, null=True)

    departure_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    passengers = models.PositiveIntegerField(default=1)

    CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first', 'First Class'),
    ]
    travel_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='economy')
    travel_class_ar = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.from_city_ar and self.from_city:
            self.from_city_ar = translator.translate(self.from_city, dest='ar').text
        if not self.to_city_ar and self.to_city:
            self.to_city_ar = translator.translate(self.to_city, dest='ar').text
        if not self.travel_class_ar and self.travel_class:
            # نترجم قيمة الدرجة فقط لو مش مترجمة
            self.travel_class_ar = translator.translate(self.get_travel_class_display(), dest='ar').text
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.from_city} → {self.to_city} ({self.departure_date})"
    




 


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField()
    description_ar = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=255)
    location_ar = models.CharField(max_length=255, blank=True, null=True)

    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    available_to = models.DateField()

    # Amenities
    wifi = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    prayer_room = models.BooleanField(default=False)
    beach_access = models.BooleanField(default=False)

    check_in = models.DateField()
    check_out = models.DateField()

    # Optional image
    image = models.ImageField(upload_to="hotels/", blank=True, null=True)
    links = models.ManyToManyField(Link, blank=True)

    def __str__(self):
        return self.name
