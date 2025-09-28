from rest_framework import serializers
from .models import (
    Transportation, HomePage, News, Video, Career,
    ContactUs, Portfolio, TravelTicket, HajjOmrah,
    Retail, Travelpackages, Link,FlightSearch,Hotel
)

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """Serializer يسمح بإرجاع الحقول بناءً على اللغة"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request') if hasattr(self, 'context') else None
        lang = request.query_params.get('lang') if request else None

        if lang == "ar":
            allowed = [f for f in self.fields if f.endswith('_ar')] + ['id', 'links']
            for field in list(self.fields):
                if field not in allowed:
                    self.fields.pop(field)

        elif lang == "en":
            allowed = [f for f in self.fields if not f.endswith('_ar')] + ['id', 'links']
            for field in list(self.fields):
                if field not in allowed:
                    self.fields.pop(field)



class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'label']


class TransportationSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Transportation
        fields = '__all__'


class HomePageSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = HomePage
        fields = '__all__'


class NewsSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = News
        fields = '__all__'


class VideoSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = '__all__'


class CareerSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Career
        fields = '__all__'


class ContactUsSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = ContactUs
        fields = '__all__'


class PortfolioSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Portfolio
        fields = '__all__'


class TravelTicketSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = TravelTicket
        fields = '__all__'


class HajjOmrahSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = HajjOmrah
        fields = '__all__'


class RetailSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Retail
        fields = '__all__'


class TravelpackagesSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Travelpackages
        fields = '__all__'


class FlightSearchSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = FlightSearch
        fields = '__all__'



class HotelSerializer(DynamicFieldsModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = "__all__"        