from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer, PersonSerializer, NestedSerializer

from .models import Country, City, State, Town, Person
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Nested Country Create':'/nested-create/',

		'Country List':'/country-list/',
		'Country Detail View':'/country-detail/<str:pk>/',
		'Country Create':'/country-create/',
		'Country Update':'/country-update/<str:pk>/',
		'Country Delete':'/country-delete/<str:pk>/',

		'State List':'/state-list/',
		'State Detail View':'/state-detail/<str:pk>/',
		'State Create':'/state-create/',
		'State Update':'/state-update/<str:pk>/',
		'State Delete':'/state-delete/<str:pk>/',

		'City List':'/city-list/',
		'City Detail View':'/city-detail/<str:pk>/',
		'City Create':'/city-create/',
		'City Update':'/city-update/<str:pk>/',
		'City Delete':'/city-delete/<str:pk>/',

		'Town List':'/town-list/',
		'Town Detail View':'/town-detail/<str:pk>/',
		'Town Create':'/town-create/',
		'Town Update':'/town-update/<str:pk>/',
		'Town Delete':'/town-delete/<str:pk>/',

		'Person List':'/person-list/',
		'Person Detail View':'/person-detail/<str:pk>/',
		'Person Create':'/person-create/',
		'Person Update':'/person-update/<str:pk>/',
		'Person Delete':'/person-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def countryList(request):
	countrys = Country.objects.all().order_by('-id')
	serializer = CountrySerializer(countrys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def countryDetail(request, pk):
	countrys = Country.objects.get(id=pk)
	serializer = CountrySerializer(countrys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def countryCreate(request):
	serializer = CountrySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def countryUpdate(request, pk):
	country = Country.objects.get(id=pk)
	serializer = CountrySerializer(instance=country, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def countryDelete(request, pk):
	country = Country.objects.get(id=pk)
	country.delete()

	return Response('Item succsesfully delete!')



@api_view(['GET'])
def stateList(request):
	states = State.objects.all().order_by('-id')
	serializer = StateSerializer(states, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def stateDetail(request, pk):
	states = State.objects.get(id=pk)
	serializer = StateSerializer(states, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def stateCreate(request):
	serializer = StateSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def stateUpdate(request, pk):
	state = State.objects.get(id=pk)
	serializer = StateSerializer(instance=state, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def stateDelete(request, pk):
	state = State.objects.get(id=pk)
	state.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def cityList(request):
	citys = City.objects.all().order_by('-id')
	serializer = CitySerializer(citys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def cityDetail(request, pk):
	citys = City.objects.get(id=pk)
	serializer = CitySerializer(citys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def cityCreate(request):
	serializer = CitySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def cityUpdate(request, pk):
	city = City.objects.get(id=pk)
	serializer = CitySerializer(instance=city, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def cityDelete(request, pk):
	city = City.objects.get(id=pk)
	city.delete()

	return Response('Item succsesfully delete!')

@api_view(['GET'])
def townList(request):
	towns = Town.objects.all().order_by('-id')
	serializer = TownSerializer(towns, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def townDetail(request, pk):
	towns = Town.objects.get(id=pk)
	serializer = TownSerializer(towns, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def townCreate(request):
	serializer = TownSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def townUpdate(request, pk):
	town = Town.objects.get(id=pk)
	serializer = TownSerializer(instance=town, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def townDelete(request, pk):
	town = Town.objects.get(id=pk)
	town.delete()

	return Response('Item succsesfully delete!')

@api_view(['GET'])
def personList(request):
	persons = Person.objects.all().order_by('-id')
	serializer = PersonSerializer(persons, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def personDetail(request, pk):
	persons = Person.objects.get(id=pk)
	serializer = PersonSerializer(persons, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def personCreate(request):
	serializer = PersonSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def personUpdate(request, pk):
	person = Person.objects.get(id=pk)
	serializer = PersonSerializer(instance=person, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def personDelete(request, pk):
	person = Person.objects.get(id=pk)
	person.delete()

	return Response('Item succsesfully delete!')


@api_view(['POST'])
def nestedCreate(request):
	country      = NestedSerializer(data=request.data)
	if country.is_valid():
		country.save()
	else:
		print('\n\nnot valid\n\n')
	return Response(country.data)



# {
#     "name": "Indighjjhjhjanested",
#     "description": "asdmaksdk",
#     "population": 89,
#     "gdp": 675.76,
#     "state": [
#         {
#             "name": "hbjvh",
#             "description": "hjbvhv",
#             "population": 788,
#             "gdp": 677.0,
#             "city": [
#                 {
#                     "name": "sdsd",
#                     "description": "fsdfsdfv",
#                     "population": 3434,
#                     "gdp": 3434.0,
#                     "pin_code": "34343"
#                 }
#             ]
#         }
#     ]
# }