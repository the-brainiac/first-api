from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

	# path('nested-create/', views.nestedCreate, name="nested-create"),
	path('nested-create/', views.NestedCreate.as_view(), name="nested-create"),

	path('country-list/', views.countryList, name="country-list"),
	path('country-detail/<str:pk>/', views.countryDetail, name="country-detail"),
	path('country-create/', views.countryCreate, name="country-create"),
	path('country-update/<str:pk>/', views.countryUpdate, name="country-update"),
	path('country-delete/<str:pk>/', views.countryDelete, name="country-delete"),

	path('state-list/', views.stateList, name="state-list"),
	path('state-detail/<str:pk>/', views.stateDetail, name="state-detail"),
	path('state-create/', views.stateCreate, name="state-create"),
	path('state-update/<str:pk>/', views.stateUpdate, name="state-update"),
	path('state-delete/<str:pk>/', views.stateDelete, name="state-delete"),

	path('city-list/', views.cityList, name="city-list"),
	path('city-detail/<str:pk>/', views.cityDetail, name="city-detail"),
	path('city-create/', views.cityCreate, name="city-create"),
	path('city-update/<str:pk>/', views.cityUpdate, name="city-update"),
	path('city-delete/<str:pk>/', views.cityDelete, name="city-delete"),

	path('town-list/', views.townList, name="town-list"),
	path('town-detail/<str:pk>/', views.townDetail, name="town-detail"),
	path('town-create/', views.townCreate, name="town-create"),
	path('town-update/<str:pk>/', views.townUpdate, name="town-update"),
	path('town-delete/<str:pk>/', views.townDelete, name="town-delete"),

	path('person-list/', views.personList, name="person-list"),
	path('person-detail/<str:pk>/', views.personDetail, name="person-detail"),
	path('person-create/', views.personCreate, name="person-create"),
	path('person-update/<str:pk>/', views.personUpdate, name="person-update"),
	path('person-delete/<str:pk>/', views.personDelete, name="person-delete"),
]