from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

	# path('nested-create/', views.nestedCreate, name="nested-create"),
	path('nested-create/', views.NestedCreate.as_view(), name="nested-create"),
	path('nested-update/<str:pk>', views.NestedUpdate.as_view(), name="nested-update"),

	path('country-list/', views.countryList.as_view(), name="country-list"),
	path('country-detail/<str:pk>/', views.countryDetail.as_view(), name="country-detail"),
	path('country-create/', views.countryCreate.as_view(), name="country-create"),
	path('country-update/<str:pk>/', views.countryUpdate.as_view(), name="country-update"),
	path('country-delete/<str:pk>/', views.countryDelete.as_view(), name="country-delete"),

	path('state-list/', views.stateList.as_view(), name="state-list"),
	path('state-detail/<str:pk>/', views.stateDetail.as_view(), name="state-detail"),
	path('state-create/', views.stateCreate.as_view(), name="state-create"),
	path('state-update/<str:pk>/', views.stateUpdate.as_view(), name="state-update"),
	path('state-delete/<str:pk>/', views.stateDelete.as_view(), name="state-delete"),

	path('city-list/', views.cityList.as_view(), name="city-list"),
	path('city-detail/<str:pk>/', views.cityDetail.as_view(), name="city-detail"),
	path('city-create/', views.cityCreate.as_view(), name="city-create"),
	path('city-update/<str:pk>/', views.cityUpdate, name="city-update"),
	path('city-delete/<str:pk>/', views.cityDelete, name="city-delete"),

	path('town-list/', views.townList.as_view(), name="town-list"),
	path('town-detail/<str:pk>/', views.townDetail.as_view(), name="town-detail"),
	path('town-create/', views.townCreate.as_view(), name="town-create"),
	path('town-update/<str:pk>/', views.townUpdate.as_view(), name="town-update"),
	path('town-delete/<str:pk>/', views.townDelete.as_view(), name="town-delete"),

	path('person-list/', views.personList.as_view(), name="person-list"),
	path('person-detail/<str:pk>/', views.personDetail.as_view(), name="person-detail"),
	path('person-create/', views.personCreate.as_view(), name="person-create"),
	path('person-update/<str:pk>/', views.personUpdate.as_view(), name="person-update"),
	path('person-delete/<str:pk>/', views.personDelete.as_view(), name="person-delete"),
]