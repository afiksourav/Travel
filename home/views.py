
from os import name
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q




# Create your views here.
def home(request):
    tour_places = Tour_place.objects.all()
    footer = Footer_items.objects.first()
    context = {'tour_place':tour_places,'footer':footer}
    return render(request,'home.html',context)


def see_place(request,pk):
    try:
        see_plac = see_places.objects.get(name=pk)
        dis_plac = District_specific_place.objects.filter(name = pk)
        name = str(see_plac.name)
        context = {'see_place':see_plac, 'name':name,'dis_place':dis_plac}
    except:
        context = {}
    return render(request,'see_place.html',context)

def place_details(request,pk):
    if request.method == 'POST':
        description = request.POST.get('description')
        rating_place = request.POST.get('rating_place')
        dis_place = District_specific_place.objects.get(id=pk)
    
        rating = Review.objects.filter(district_place=pk)

        if rating.filter(name = request.user).exists():
            exists_data = rating.filter(name=request.user).first()

            exists_data.description = description
            exists_data.rating_place = rating_place
            exists_data.save()
        else:
            user_profile_get = UserInfo.objects.get(user = request.user)
            user_review = Review(       
                    description = description,
                    rating_place = rating_place,
                    district_place=dis_place,
                    name= request.user,  
                    user_profile = user_profile_get 
                )
            user_review.save()
        return redirect('place_details', pk)

    videos = District_details_video.objects.get(name=pk)
    gallary_photo = District_details_gallary.objects.filter(name = pk)
    rating = Review.objects.filter(district_place=pk)

    user_submitted = False
    exists_data = None

    if request.user.is_authenticated:
        if rating.filter(name = request.user).exists():
            user_submitted = True
            exists_data = rating.filter(name=request.user).first()
    context = {
        'videos':videos,
        'gallary_photo':gallary_photo,
        'rating':rating,
        'user_submitted':user_submitted,
        'exists_data':exists_data
    } 
    return render(request,'district_place_details.html',context)


# reg

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        city = request.POST.get('city')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if not User.objects.filter(username = username).exists():
                if not UserInfo.objects.filter(Phone_Number = phone_number).exists():
                    user_now = User.objects.create_user(username = username, password = password, email = email)
                    user_info_now = UserInfo(
                        user = user_now, 
                        Phone_Number = phone_number,
                        country = country,
                        city = city,
                        full_name = fullname
                    )
                    user_now.save()
                    user_info_now.save()
                    return redirect('login')
                else:
                    messages.error(request, "Phone number already exists")
            else:
                messages.error(request, "Username already exists")
        else:
            messages.error(request, "Two password field didn't match")
    return render(request,'users/register.html' )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if request.user.is_authenticated:
            contact_now = UserContact(
            subject = subject,
             message = message,
             user = request.user
             )

        else:
            contact_now = anonymousContact(
            name = name,
            email =email,
            number = number,
            subject = subject,
            message = message
            )
        contact_now.save()
        messages.success(request, "thank your for your response")
        return redirect('contact')   
    return render(request,'contact.html')

@login_required
def booking(request):
    if request.method == 'POST':
        place_name=request.POST.get('place_name')
        guests_number=request.POST.get('guests_number')
        check_in=request.POST.get('check_in')
        check_out = request.POST.get('check_out')
    
        bookings_of_this_user = Booking_user.objects.filter(user= request.user)

        if bookings_of_this_user:
            exists_data = bookings_of_this_user.filter(status='in_progress').first()
            if exists_data:
                  
                exists_data.guests_number = guests_number
                exists_data.check_in = check_in
                exists_data.check_out = check_out
                exists_data.save()
                messages.success(request, "Booking data Updated")
                return redirect('booking')
        else:
            place = District_specific_place.objects.get(id=place_name) #bujhe nai
            book = Booking_user(
                place_name = place,
                guests_number = guests_number,
                check_in = check_in,
                check_out = check_out,
                user = request.user
                )
            book.save()
            messages.success(request, "Booking Crated")
            return redirect('booking')
    
    all_specific_palces = District_specific_place.objects.all()

    user_submitted = False
    exists_data = None
    bookings_of_this_user = Booking_user.objects.filter(user= request.user)

    if bookings_of_this_user:
        exists_data = bookings_of_this_user.filter(status='in_progress').first()
        if exists_data:
            user_submitted = True

    context = {
        'all_specific_palces':all_specific_palces,
        'user_submitted':user_submitted,
        'exists_data':exists_data
    } 
    return render(request,'booking.html',context)


def tour_packages(request):
    package = Packages.objects.all()
    context = {'package':package}
    return render (request,'packages.html',context)

def package_place(request,pk):
    package_items = PackageDetail_S.objects.filter(package_item=pk)
    context = {'package_item':package_items}
    return render (request,'packages_place.html',context)

def package_details_place(request,pk):
    package_box = PackageDetail_Place.objects.get(package_item=pk)

    try:
        package_gallery = Package_Gallery.objects.get(package_items=package_box)
    except:
        package_gallery = None
    


    context = {
        'package_box':package_box, 
        'package_gallery' : package_gallery
    }

    return render (request,'packages_details.html',context)

def booking_package(request,pk):
    booking     = PackageDetail_Place.objects.get(id=pk)
    place_name  = booking.package_item
    description = booking.description
    member      = booking.package_item.member
    price       = booking.package_item.price
    package_name= booking.package_item.package_item
    
    
    book = Booking_Package(
                package_name = package_name,
                place_name   = place_name,
                description  = description,
                mamber       = member,
                price        = price,
                user = request.user
    )
    book.save()
    messages.success(request, "Booking package successful created")

    return redirect("package_details_place", pk=booking.package_item.id)










