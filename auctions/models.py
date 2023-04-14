from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.category_name}"

class Listing(models.Model):
    listing_name = models.CharField(max_length=70, null=False)
    listing_desc =  models.CharField(max_length=2000, null=False)
    listing_category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True, default="Custom")
    bid = models.FloatField(null=False, default=0.00)
    imgurl = models.CharField( max_length= 500 ,null=True,default="https://icon-library.com/images/no-picture-available-icon/no-picture-available-icon-1.jpg")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE , blank= True, null=True , related_name="user")
    isActive = models.BooleanField(default=True)
  
    def __str__(self):
        return f"{self.id} {self.listing_name}"
    

class Watchlist(models.Model):
    user_watchlist = models.ForeignKey(User , on_delete=models.CASCADE)
    listing_watchlist = models.ForeignKey(Listing , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.user_watchlist} {self.listing_watchlist}"
    
class Comments(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_listing =models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id} {self.comment_user} {self.comment_listing} {self.comment}"
    
class Bids(models.Model):
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE , default=User.objects.get(username='mathewalex'))
    bid_title =models.ForeignKey(Listing, on_delete=models.CASCADE, primary_key=True)
    bid_amount = models.FloatField(null=False , default=0)
    bid_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.bid_title} by {self.bid_user} {self.bid_amount}"
    

