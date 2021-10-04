from os import name
import user
from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import redirect
from home.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    profileUser = UserInfo.objects.get(user=request.user)
    context={'i':profileUser}
    return render(request, 'user.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        country = request.POST.get('country')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        Email = request.POST.get('Email')
        city = request.POST.get('city')
        Phone_Number = request.POST.get('Phone_Number')
        image = request.FILES['image']

        exists_data = UserInfo.objects.get(user=request.user)
        exists_data.full_name = full_name
        exists_data.country = country
        exists_data.dob = dob
        exists_data.address = address
        exists_data.Email = Email
        exists_data.city = city
        exists_data.Phone_Number = Phone_Number
        exists_data.profile_pic = image
           
        
        exists_data.save()

    current_user_data = UserInfo.objects.get(user=request.user)
    context = {'i':current_user_data}
    return render(request,'edit_profile.html', context)


@login_required
def user_rating(request):
    user_review = Review.objects.filter(name=request.user)
    
    context={'user_review':user_review}
    return render (request, 'user_rating.html',context)

@login_required
def booking_status(request):
    book =Booking_user.objects.filter(user=request.user)
    package_booking= Booking_Package.objects.filter(user=request.user)
    print(package_booking)
    return render (request, 'user_booking.html',{'booking':book,'package_booking':package_booking})

@login_required
def RemoveItem(request, pk):
    delete_item = Booking_user.objects.get(user=request.user,place_name=pk)
    delete_item.delete()
    return redirect("booking_status")

@login_required
def Remove_package(request, pk):
    
    delete_package = Booking_Package.objects.get(user=request.user,id=pk)
    delete_package.delete()
    return redirect("booking_status")








