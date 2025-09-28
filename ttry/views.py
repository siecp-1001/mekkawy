from rest_framework import viewsets
from .models import (
    Hotel, Transportation, HomePage, News, Video, Career,
    ContactUs, Portfolio, TravelTicket, HajjOmrah,
    Retail, Travelpackages,FlightSearch
)
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    HotelSerializer, TransportationSerializer, HomePageSerializer, NewsSerializer, VideoSerializer,
    CareerSerializer, ContactUsSerializer, PortfolioSerializer, TravelTicketSerializer,
    HajjOmrahSerializer, RetailSerializer, TravelpackagesSerializer,FlightSearchSerializer
)


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet يمرر request للـ serializer علشان نفلتر حسب اللغة"""
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class TransportationViewSet(viewsets.ModelViewSet):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        pickup_date = request.query_params.get('pickup_date')
        return_date = request.query_params.get('return_date')
        pickup_location = request.query_params.get('pickup_location')
        cartype = request.query_params.get('cartype')

        qs = self.queryset

        if pickup_date:
            qs = qs.filter(pickup_date=pickup_date)

        if return_date:
            qs = qs.filter(return_date=return_date)

        if pickup_location:
            qs = qs.filter(pickup_location__icontains=pickup_location)

        if cartype:
            qs = qs.filter(cartype__icontains=cartype)

        serializer = self.get_serializer(qs, many=True, context={'request': request})
        return Response(serializer.data)


class HomePageViewSet(BaseViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer


class NewsViewSet(BaseViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class VideoViewSet(BaseViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CareerViewSet(BaseViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class ContactUsViewSet(BaseViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class PortfolioViewSet(BaseViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class TravelTicketViewSet(BaseViewSet):
    queryset = TravelTicket.objects.all()
    serializer_class = TravelTicketSerializer


class HajjOmrahViewSet(BaseViewSet):
    queryset = HajjOmrah.objects.all()
    serializer_class = HajjOmrahSerializer


class RetailViewSet(BaseViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer


class TravelpackagesViewSet(viewsets.ModelViewSet):
    queryset = Travelpackages.objects.all()
    serializer_class = TravelpackagesSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        name = request.query_params.get("name")
        lang = request.query_params.get("lang", "en")

        qs = self.queryset

        if name:
            if lang == "ar":
                qs = qs.filter(product_name_ar__icontains=name)
            else:
                qs = qs.filter(product_name__icontains=name)

        serializer = self.get_serializer(qs, many=True, context={"request": request})
        return Response(serializer.data)


class FlightSearchViewSet(BaseViewSet):
    queryset = FlightSearch.objects.all()
    serializer_class = FlightSearchSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        from_city = request.query_params.get("from_city")
        to_city = request.query_params.get("to_city")
        departure_date = request.query_params.get("departure_date")
        return_date = request.query_params.get("return_date")
        travel_class = request.query_params.get("travel_class")
        lang = request.query_params.get("lang", "en")

        qs = self.queryset

        if from_city:
            if lang == "ar":
                qs = qs.filter(from_city_ar__icontains=from_city)
            else:
                qs = qs.filter(from_city__icontains=from_city)

        if to_city:
            if lang == "ar":
                qs = qs.filter(to_city_ar__icontains=to_city)
            else:
                qs = qs.filter(to_city__icontains=to_city)

        if departure_date:
            qs = qs.filter(departure_date=departure_date)

        if return_date:
            qs = qs.filter(return_date=return_date)

        if travel_class:
            if lang == "ar":
                qs = qs.filter(travel_class_ar__icontains=travel_class)
            else:
                qs = qs.filter(travel_class__iexact=travel_class)

        serializer = self.get_serializer(qs, many=True, context={"request": request})
        return Response(serializer.data)




class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        location = request.query_params.get('location')
        check_in = request.query_params.get('check_in')
        check_out = request.query_params.get('check_out')
        guests = request.query_params.get('guests')
        rooms = request.query_params.get('rooms')

        qs = self.queryset

        # 🔎 فلترة بالموقع
        if location:
            qs = qs.filter(location__icontains=location)

        # 🔎 فلترة بالتواريخ (لو الفندق عنده available_from و available_to)
        if check_in and check_out:
            qs = qs.filter(
                available_from__lte=check_in,
                available_to__gte=check_out
            )

        # 🔎 فلترة بالعدد المطلوب من الضيوف
        if guests:
            qs = qs.filter(max_guests__gte=int(guests))

        # 🔎 فلترة بالعدد المطلوب من الغرف
        if rooms:
            qs = qs.filter(num_rooms__gte=int(rooms))

        serializer = self.get_serializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def locations(self, request):
        lang = request.query_params.get('lang', 'en')
        if lang == "ar":
            locations = Hotel.objects.values_list("location_ar", flat=True).distinct()
        else:
            locations = Hotel.objects.values_list("location", flat=True).distinct()
        
        return Response({"locations": [loc for loc in locations if loc]})
