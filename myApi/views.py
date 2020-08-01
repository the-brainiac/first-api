from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer, PersonSerializer, NestedSerializer

from .models import Country, City, State, Town, Person
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Nested Country Create':'/myApi/nested-create/',

		'Country List':'/myApi/country-list/',
		'Country Detail View':'/myApi/country-detail/<str:pk>/',
		'Country Create':'/myApi/country-create/',
		'Country Update':'/myApi/country-update/<str:pk>/',
		'Country Delete':'/myApi/country-delete/<str:pk>/',

		'State List':'/myApi/state-list/',
		'State Detail View':'/myApi/state-detail/<str:pk>/',
		'State Create':'/myApi/state-create/',
		'State Update':'/myApi/state-update/<str:pk>/',
		'State Delete':'/myApi/state-delete/<str:pk>/',

		'City List':'/myApi/city-list/',
		'City Detail View':'/myApi/city-detail/<str:pk>/',
		'City Create':'/myApi/city-create/',
		'City Update':'/myApi/city-update/<str:pk>/',
		'City Delete':'/myApi/city-delete/<str:pk>/',

		'Town List':'/myApi/town-list/',
		'Town Detail View':'/myApi/town-detail/<str:pk>/',
		'Town Create':'/myApi/town-create/',
		'Town Update':'/myApi/town-update/<str:pk>/',
		'Town Delete':'/myApi/town-delete/<str:pk>/',

		'Person List':'/myApi/person-list/',
		'Person Detail View':'/myApi/person-detail/<str:pk>/',
		'Person Create':'/myApi/person-create/',
		'Person Update':'/myApi/person-update/<str:pk>/',
		'Person Delete':'/myApi/person-delete/<str:pk>/',
		}

	return Response(api_urls)

class countryList(ListAPIView):
	queryset         = Country.objects.all().order_by('-id')
	serializer_class = CountrySerializer

class countryDetail(RetrieveAPIView):
	queryset         = Country
	serializer_class = CountrySerializer

class countryCreate(CreateAPIView):
	serializer_class = CountrySerializer

class countryUpdate(UpdateAPIView):
	queryset         = Country
	serializer_class = CountrySerializer

class countryDelete(DestroyAPIView):
	queryset         = Country



class stateList(ListAPIView):
	queryset         = State.objects.all().order_by('-id')
	serializer_class = StateSerializer

class stateDetail(RetrieveAPIView):
	queryset         = State
	serializer_class = StateSerializer

class stateCreate(CreateAPIView):
	serializer_class = StateSerializer

class stateUpdate(UpdateAPIView):
	queryset         = State
	serializer_class = StateSerializer

class stateDelete(DestroyAPIView):
	queryset         = State


class cityList(ListAPIView):
	queryset         = City.objects.all().order_by('-id')
	serializer_class = CitySerializer

class cityDetail(RetrieveAPIView):
	queryset         = City
	serializer_class = CitySerializer

class cityCreate(CreateAPIView):
	serializer_class = CitySerializer

class cityUpdate(UpdateAPIView):
	queryset         = City
	serializer_class = CitySerializer

class cityDelete(DestroyAPIView):
	queryset         = City



class townList(ListAPIView):
	queryset         = Town.objects.all().order_by('-id')
	serializer_class = TownSerializer

class townDetail(RetrieveAPIView):
	queryset         = Town
	serializer_class = TownSerializer

class townCreate(CreateAPIView):
	serializer_class = TownSerializer

class townUpdate(UpdateAPIView):
	queryset         = Town
	serializer_class = TownSerializer

class townDelete(DestroyAPIView):
	queryset         = Town



class personList(ListAPIView):
	queryset         = Person.objects.all().order_by('-id')
	serializer_class = PersonSerializer

class personDetail(RetrieveAPIView):
	queryset         = Person
	serializer_class = PersonSerializer

class personCreate(CreateAPIView):
	serializer_class = PersonSerializer

class personUpdate(UpdateAPIView):
	queryset         = Person
	serializer_class = PersonSerializer

class personDelete(DestroyAPIView):
	queryset         = Person



class NestedCreate(CreateAPIView):
	serializer_class = NestedSerializer

		
class NestedUpdate(UpdateAPIView):
	serializer_class = NestedSerializer
	queryset         = Country

"""
{
    "name": "India1",
    "description": "asdmaksdk",
    "population": 89,
    "gdp": 675.76,
    "state": [
        {
            "name": "state1",
            "description": "hjbvhv",
            "population": 788,
            "gdp": 677.0,
            "city": [
                {
                    "name": "city1",
                    "description": "fsdfsdfv",
                    "population": 3434,
                    "gdp": 3434.0,
                    "pin_code": "343431"
                }
            ]
        }
    ]
}
"""