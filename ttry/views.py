from rest_framework import viewsets
from .models import *
from .serializers import *

class TransportationViewSet(viewsets.ModelViewSet):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class TravelTicketViewSet(viewsets.ModelViewSet):
    queryset = TravelTicket.objects.all()
    serializer_class = TravelTicketSerializer

class HajjOmrahViewSet(viewsets.ModelViewSet):
    queryset = HajjOmrah.objects.all()
    serializer_class = HajjOmrahSerializer

class RetailViewSet(viewsets.ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer



class TravelpackagesViewSet(viewsets.ModelViewSet):
    queryset = Travelpackages.objects.all()
    serializer_class = TravelpackagesSerializer