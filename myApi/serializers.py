from rest_framework import serializers
from .models import Country, City, State, Town, Person


####################################
###     For seperate models      ###
####################################

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model   = Country
		fields  = '__all__'

class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model   = State
		fields  = '__all__'

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model   = City
		fields  = '__all__'

class TownSerializer(serializers.ModelSerializer):
	class Meta:
		model   = Town
		fields  = '__all__'

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model   = Person
		fields  = '__all__'



####################################
###   For nested Country field   ###
####################################

class nestedCitySerializer(serializers.ModelSerializer):
	class Meta:
		model   = City
		fields  = ['id', 'name', 'description', 'population', 'gdp','pin_code']


class NestedStateSerializer(serializers.ModelSerializer):
	city   = nestedCitySerializer(many=True)

	class Meta:
		model   = State
		fields  = ['id', 'name', 'description', 'population', 'gdp', 'city']

	def create(self, validated_data):
		state_data = validated_data
		cities_data = state_data.pop('city')
		state = State.objects.create(country=country, **state_data)

		for city_data in cities_data:
			city = City.objects.create(state=state, **city_data)

		return state

class NestedSerializer(serializers.ModelSerializer):
	state  = NestedStateSerializer(many=True,required=False)
	
	class Meta:
		model   = Country
		fields  = ['id', 'name', 'description', 'population', 'gdp', 'state']

	def create(self, country_data):
		try:
			states_data   = country_data.pop('state')
		except KeyError:
			states_data   = []

		country      = Country.objects.create(**country_data)
		for state_data in states_data:
			cities_data = state_data.pop('city')
			state = State.objects.create(country=country, **state_data)
			for city_data in cities_data:
				city = City.objects.create(state=state, country=country, **city_data)
		return country
		
	"""
	def update(self, instance, country_data):
		try:
			states_data   = country_data.pop('state')
		except KeyError:
			states_data   = []


		instance.description = country_data.get('description',instance.description)
		instance.population = country_data.get('population',instance.population)
		instance.gdp = country_data.get('gdp',instance.gdp)
		instance.save()

		for state_data in states_data:
			cities_data = state_data.pop('city')
			state = State.objects.get(name=state_data['name'])

			state['description'] = state_data['description']
			state['population'] = state_data['population']
			state['gdp'] = state_data['gdp']
			if state.is_valid():
				state.save()

			for city_data in cities_data:
				city = City.objects.get(nsme=city_data['name'])

				city['description'] = city_data['description']
				city['population'] = city_data['population']
				city['gdp'] = city_data['gdp']
				city['pin_code'] = city_data['pin_code']
				if city.is_valid():
					city.save()
		return country
	"""