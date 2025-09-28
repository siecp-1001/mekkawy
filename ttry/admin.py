from django.contrib import admin
from django import forms
from .models import (
    Transportation,
    HomePage,
    News,
    Video,
    Career,
    ContactUs,
    Portfolio,
    TravelTicket,
    HajjOmrah,
    Retail,
    Travelpackages,
    Link,
    FlightSearch,
    Hotel
)


# Function to build a form with checkbox widget for links
def make_links_form(model):
    class LinksForm(forms.ModelForm):
        class Meta:
            model = Link
            fields = '__all__'
            widgets = {
                'links': forms.CheckboxSelectMultiple
            }
    return LinksForm


# Admin classes
class HajjOmrahAdmin(admin.ModelAdmin):
    form = make_links_form(HajjOmrah)

class HotelAdmin(admin.ModelAdmin):
    form = make_links_form(Hotel)

class FlightSearchAdmin(admin.ModelAdmin):
    form = make_links_form(FlightSearch)

class TravelpackagesAdmin(admin.ModelAdmin):
    form = make_links_form(Travelpackages)


class TransportationAdmin(admin.ModelAdmin):
    form = make_links_form(Transportation)


class HomePageAdmin(admin.ModelAdmin):
    form = make_links_form(HomePage)


class NewsAdmin(admin.ModelAdmin):
    form = make_links_form(News)


class VideoAdmin(admin.ModelAdmin):
    form = make_links_form(Video)


class CareerAdmin(admin.ModelAdmin):
    form = make_links_form(Career)


class ContactUsAdmin(admin.ModelAdmin):
    form = make_links_form(ContactUs)


class PortfolioAdmin(admin.ModelAdmin):
    form = make_links_form(Portfolio)


class TravelTicketAdmin(admin.ModelAdmin):
    form = make_links_form(TravelTicket)


class RetailAdmin(admin.ModelAdmin):
    form = make_links_form(Retail)


# Register
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(TravelTicket, TravelTicketAdmin)
admin.site.register(HajjOmrah, HajjOmrahAdmin)
admin.site.register(Retail, RetailAdmin)
admin.site.register(Travelpackages, TravelpackagesAdmin)
admin.site.register(FlightSearch, FlightSearchAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Link)
