from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name = "create"),
    path("categories/", views.categories , name="categories"),
    path("listing", views.listing, name="listing"),
    path("watchlist",views.watchlist, name="watchlist"),
    path("watchlist_add", views.addwatchlist, name="addwatchlist"),
    path("watchlist_remove", views.removewatchlist, name="removewatchlist"),
    path("add_comment", views.add_comment, name = "add_comment"),
    path("bid", views.bid, name="bid"),
    path("close_listing", views.close_listing , name="close_listing"),
    path("closedauction_details", views.bid_winner, name="bid_winner")
]
