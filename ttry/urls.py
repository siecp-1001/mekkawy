from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'transportation', TransportationViewSet)
router.register(r'homepage', HomePageViewSet)
router.register(r'news', NewsViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'careers', CareerViewSet)
router.register(r'contact-us', ContactUsViewSet)
router.register(r'portfolio', PortfolioViewSet)
router.register(r'travel-tickets', TravelTicketViewSet)
router.register(r'hajj-omrah', HajjOmrahViewSet)
router.register(r'retail', RetailViewSet)
router.register(r'Travel-packages', TravelpackagesViewSet)
router.register(r'Flight-Search', FlightSearchViewSet)
router.register(r'hotels', HotelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
