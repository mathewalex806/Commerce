from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.models import User,Category,Listing
from auctions.models import *

from .models import User


def index(request):
    return render(request, "auctions/index.html",{"item":Listing.objects.filter(isActive = True),"cat":Category.objects.all()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "GET":
        return render(request,"auctions/create.html",{"category":Category.objects.all()})
    
    elif request.method == "POST":
        title = request.POST["title"]
        description = request.POST["desc"]
        category = request.POST["listing_category"]
        img = request.POST["link"]
        price = request.POST["bid"]
        user = request.user
    categoryData = Category.objects.get(category_name = category)

    

    f = Listing(
        listing_name = title,
        listing_desc = description,
        listing_category = categoryData,
        bid = price,
        imgurl = img,
        owner = user
    )
    f.save()
    j= Bids(
        bid_user = User.objects.get(username = user),
        bid_title = Listing.objects.get(listing_name = title),
        bid_amount = price
        )
    j.save()
    return HttpResponseRedirect(reverse("index"))


def categories(request):
    if request.method == "POST":
        category = request.POST["category"]
        categoryData = Category.objects.get(category_name = category)
        item_data = Listing.objects.filter(listing_category=categoryData)
        return render(request, "auctions/categories.html", {"list_item":item_data , "q":item_data.first()})
    

    return render(request , "auctions/categories.html",{"cat": Category.objects.all() })


def listing(request):
    title_name =""
    if request.method == "POST":
        title = request.POST["title"]
        title_name = title 
        q = Listing.objects.get(listing_name = title)
        list_title = q.listing_name
        list_desc = q.listing_desc
        list_category = q.listing_category
        list_img = q.imgurl
        list_bid = q.bid
        list_owner = q.owner
        list_created = q.created_at
        return render(request, "auctions/listing.html", {"list_title":list_title, "list_desc":list_desc, "list_cat":list_category, "list_img":list_img, "list_bid":list_bid, "list_owner":list_owner, "list_created":list_created , "comments_query":Comments.objects.all(),"bid_query":Bids.objects.get(bid_title = Listing.objects.get(listing_name = title))})
    else:
        s= Listing.objects.get(listing_name = title_name)
        list_title = s.listing_name
        list_desc = s.listing_desc
        list_category = s.listing_category
        list_img = s.imgurl
        list_bid = s.bid
        list_owner = s.owner
        list_created = s.created_at
        return render(request, "auctions/listing.html", {"list_title":list_title, "list_desc":list_desc, "list_cat":list_category, "list_img":list_img, "list_bid":list_bid, "list_owner":list_owner, "list_created":list_created , "message":"", "comments_query":Comments.objects.all(),"bid_query":Bids.objects.get(bid_title = Listing.objects.get(listing_name = list_title))})


    
def watchlist(request):
    a=[]
    if request.method =="POST":
        username_watchlist = request.POST["username"]
        q = Watchlist.objects.all()
        for i in q:
            if i.listing_watchlist.owner != username_watchlist:

                if i.user_watchlist.username == username_watchlist:
                    title = i.listing_watchlist.listing_name
                    cat = i.listing_watchlist.listing_category
                    bid = i.listing_watchlist.bid
                    img = i.listing_watchlist.imgurl
                    owner = i.listing_watchlist.owner
                    created = i.listing_watchlist.created_at
                    a.append((title,cat,bid,img,owner,created))
        return render(request, "auctions/watchlist.html", {"query":a})

    return render(request,"auctions/watchlist.html",{"watchlist":Watchlist.objects.all()})

def addwatchlist(request):
    if request.method == "POST":
        username_watchlist = request.POST["user_watch"]
        title_watchlist = request.POST["list_watch"]
        
        try:
            f = Watchlist( user_watchlist = User.objects.get(username = username_watchlist),listing_watchlist= Listing.objects.get(listing_name=title_watchlist))
            f.save()
            message = "Added To Your Watchlist"
        except:
            message = "Failed To Add Listing To Your Watchlist"
        return render(request, "auctions/watchlist.html", {"message":message})
    
def removewatchlist(request):
    if request.method == "POST":
        username_watchlist = request.POST["user_watch"]
        title_watchlist = request.POST["list_watch"]
        s= Watchlist.objects.get(user_watchlist = User.objects.get(username = username_watchlist), listing_watchlist =Listing.objects.get(listing_name = title_watchlist))
        s.delete()
        return render(request, "auctions/watchlist.html", {"message":"Removed item from Watchlist"})
               
def add_comment(request):
    if request.method == "POST":
        comment = request.POST["comment"]
        username = request.POST["username"]
        title = request.POST["title"]
        f = Comments(comment_user = User.objects.get(username = username), comment_listing = Listing.objects.get(listing_name = title) , comment = comment)
        f.save()
        return render (request,"auctions/text.html",{"message":"Added your comment"})

def bid(request):
    if request.method == "POST":
        username = request.POST["user"]
        username_query = User.objects.get(username = username)
        title = request.POST["title"]
        title_query = Listing.objects.get(listing_name = title)
        bid = request.POST["bid"]
        q= Bids.objects.get(bid_title = Listing.objects.get(listing_name = title))
        q_bid = q.bid_amount
        a= Listing.objects.get(listing_name = title)
        if int(q_bid)>= int(bid) :
            return render(request,"auctions/listing.html",{"list_title":a.listing_name,"list_desc":a.listing_desc, "list_cat": a.listing_category, "list_img":a.imgurl, "list_bid":a.bid, "list_owner":a.owner, "list_created":a.created_at , "message":"Place a bid greater than the existing bid.", "comments_query":Comments.objects.all()})
        else:
            f= Bids(bid_user = username_query,bid_title = title_query, bid_amount = int(bid))
            f.save()
            return render(request,"auctions/listing.html",{"list_title":a.listing_name,"list_desc":a.listing_desc, "list_cat": a.listing_category, "list_img":a.imgurl, "list_bid":a.bid, "list_owner":a.owner, "list_created":a.created_at , "message":"You're bid was successfully added.", "comments_query":Comments.objects.all(),"bid_query":Bids.objects.get(bid_title = Listing.objects.get(listing_name = title))})


def close_listing(request):
    if request.method == "POST":
        title_close = request.POST["title_close"]
        q = Listing.objects.filter(listing_name = title_close ).update(isActive = False)
        return render(request,"auctions/text.html",{"message":"Closed Current Listing","listings":Listing.objects.filter(isActive = False)})
    else:
        return render(request,"auctions/text.html",{"listings":Listing.objects.filter(isActive = False)})
        
        
def bid_winner(request):
    if request.method == "POST":
        title = request.POST["title"]
        return render(request,"auctions/closedauction_deets.html",{"bid_query": Bids.objects.get(bid_title = Listing.objects.get(listing_name = title)), "list_query":Listing.objects.get(listing_name = title)})
        