from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Tour_place(models.Model):
    place_name = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to = "images", editable=True)
    
    def __str__(self):
        return self.place_name

    def save(self):
        super().save()
        img  = Image.open(self.image.path)
        if img.width > 300 or img.height> 364:
            output_size = (300, 364)
            img.thumbnail(output_size)
            img.save(self.image.path)

class see_places(models.Model):
    name = models.ForeignKey(Tour_place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images")
    description = models.TextField()

    def __str__(self):
        return str(self.name)

class District_specific_place(models.Model):
    name = models.ForeignKey(Tour_place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images")
    District_place_name = models.CharField(max_length=50)
    description = models.TextField()
    RATING_RANGE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    ratings =models.IntegerField(choices=RATING_RANGE,)
    price = models.IntegerField()

    def __str__(self):
        return str(self.District_place_name)

class District_details_video(models.Model):
    name = models.ForeignKey(District_specific_place, on_delete=models.CASCADE)
    video = models.FileField(upload_to = "video")
    description_video = models.TextField(max_length=200)

    def __str__(self):
        return str(self.name)
    
class District_details_gallary(models.Model):
    name = models.ForeignKey(District_specific_place, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to = "gallery", null=True, blank=True)
    image2 = models.ImageField(upload_to = "gallery", null=True, blank=True)
    image3 = models.ImageField(upload_to = "gallery", null=True, blank=True)
    image4 = models.ImageField(upload_to = "gallery", null=True, blank=True)
    image5 = models.ImageField(upload_to = "gallery", null=True, blank=True)
    image6 = models.ImageField(upload_to = "gallery", null=True, blank=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return ('gallary of ' + str(self.name))





class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics', blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    Email = models.EmailField(max_length=100, blank=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250,blank=True, null=True)
    country =  models.CharField(max_length=250,blank=True, null=True)
    city =  models.CharField(max_length=100,blank=True)
    Phone_Number = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.full_name)

class Review(models.Model):
    district_place = models.ForeignKey(District_specific_place, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    description = models.TextField(max_length=500 , null=True)
    rating_place = models.IntegerField(null=True)

    def __str__(self):
        return 'User is ' + str(self.name) + ' ,place review = ' +str(self.district_place)


class anonymousContact(models.Model):
   
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    number = models.IntegerField(blank=True)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)

class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.user)

class Booking_user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place_name = models.ForeignKey(District_specific_place, on_delete=models.CASCADE)
    guests_number = models.IntegerField()
    check_in = models.DateField()
    check_out= models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS = (
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
        ('confirmed', 'Confirmed'),
        ('complete', 'Trip Complete'),
    )
    status =models.CharField(choices=STATUS, default='in_progress', max_length=255)

    def __str__(self):
        return str(self.user)

class Packages(models.Model):
    package_name= models.CharField(max_length=30,primary_key=True)
    image = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.package_name)

class PackageDetail_S(models.Model):
    package_item = models.ForeignKey(Packages, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=80)
    image = models.ImageField(upload_to = "images")
    description = models.TextField(max_length=200)
    member= models.IntegerField()
    duration= models.CharField(max_length=250)
    price= models.IntegerField()

    def __str__(self):
        return str(self.place_name) + ' ,' + str(self.package_item)

class PackageDetail_Place(models.Model):
    package_item = models.ForeignKey(PackageDetail_S, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = "images")

    def __str__(self):
        return str(self.package_item)

class Package_Gallery(models.Model):
    package_items = models.ForeignKey(PackageDetail_Place, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to = "package_gallery", null=True, blank=True)
    image2 = models.ImageField(upload_to = "package_gallery", null=True, blank=True)
    image3 = models.ImageField(upload_to = "package_gallery", null=True, blank=True)
    image4 = models.ImageField(upload_to = "package_gallery", null=True, blank=True)
    image5 = models.ImageField(upload_to = "package_gallery", null=True, blank=True)
    image6 = models.ImageField(upload_to = "package_gallery", null=True, blank=True)



class Booking_Package(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    package_name = models.ForeignKey(Packages, on_delete=models.CASCADE)
    place_name = models.ForeignKey(PackageDetail_S, on_delete=models.CASCADE)
    description= models.TextField()
    mamber = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS = (
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
        ('confirmed', 'Confirmed'),
        ('complete', 'Trip Complete'),
    )
    status =models.CharField(choices=STATUS, default='in_progress', max_length=255)




class Footer_items(models.Model):
    facebook = models.CharField(max_length=100)
    Instagram= models.CharField(max_length=100)
    Twitter= models.CharField(max_length=100)
    Linkedin= models.CharField(max_length=150)


  
    









    



    
    

