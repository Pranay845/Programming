from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('About/', views.about, name="AboutUs"),
    path('Contact/', views.contact, name="ContactUs"),
    path('Tracker/', views.tracker, name="TrackingStatus"),
    path('Search/', views.search, name="Search"),
    path('ProductView/<int:myid>', views.productview, name="ProductView"),
    path('Checkout/', views.checkout, name="Checkout"),
]
