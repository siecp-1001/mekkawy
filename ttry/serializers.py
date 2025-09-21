from rest_framework import serializers
from .models import (
    Transportation, HomePage, News, Video, Career,
    ContactUs, Portfolio, TravelTicket, HajjOmrah,
    Retail, Travelpackages, Link
)

# Central Link serializer
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'label']


class TransportationSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Transportation
        fields = '__all__'


class HomePageSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = HomePage
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class CareerSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Career
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = ContactUs
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'


class TravelTicketSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = TravelTicket
        fields = '__all__'


class HajjOmrahSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = HajjOmrah
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Retail
        fields = '__all__'


class TravelpackagesSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Travelpackages
        fields = '__all__'
