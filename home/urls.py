from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('see_place/<pk>/',views.see_place,name='see_place'),
    path('place_details/<pk>/',views.place_details,name='place_details'),
    path('contact/',views.contact,name='contact'),
    path('booking/',views.booking,name='booking'),
    path('packages/',views.tour_packages,name='packages'),
    path('package_place/<pk>/',views.package_place,name='package_place'),
    path('package_details_place/<pk>/',views.package_details_place,name='package_details_place'),
    path('booking_package/<pk>/',views.booking_package,name='booking_package'),
    




    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login_e.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'home'), name='logout'),

     #passow reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]