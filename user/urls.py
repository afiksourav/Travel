from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('user_rating/',views.user_rating,name='user_rating'),
    path('booking_status/',views.booking_status,name='booking_status'),
    path('RemoveItem/<pk>/',views.RemoveItem,name='RemoveItem'),
    path('Remove_package/<pk>/',views.Remove_package,name='Remove_package'),
]