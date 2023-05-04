from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "Home"),  #leads to home page
    path("about/", views.about, name = "aboutus"), #leads to about us section
    path("contact/", views.contact, name = "ContactUs"), #contact us page
    path("Search/", views.search, name = "Search"), #handles search query
    path("Products/", views.product, name = "Products"), #Intermediate 
    path("Checkout/", views.checkout, name = "Checkout"), #Handles checkout page
    path("Trackit/", views.track, name = "TrackYourOrder"), #Handles Tracker page
    path("Prodview1/",views.Prodview1, name= "Home appliances"), #Displays home appliances
    path("Music/", views.music, name= "music"), #displays music
    path('ayurveda/', views.ayurveda, name = "ayurveda"), #displays ayurveda
    path("Iaminsider/", views.insider, name = "insider"), #displays insider links
    path("education&learning/", views.education, name='education&learning'), #displays category of education
    path("Home_Appliances/", views.Home_App, name = "Home_Appliances"), #displays Home appliances
    path("Sports/", views.Sport, name = "Sports"), #Displays sports
    path("Clothing/", views.Cloth, name = "Clothing"), #Displays clothing url
    path("Software/", views.soft, name = "Software and Gaming"), #Displaying softwares
    path('login', views.handeLogin, name="handleLogin"), #Handles login
    path('logout', views.handelLogout, name="handleLogout"), #Handles logout
    path('collabs/', views.collab, name="collaborators"), #Diplays weblink of merchents
    path('education/', views.education, name="education"), #Displays education html
    path("grocery/", views.gro,name="Home"), #Displays grocery
    path("Book/", views.copies, name = "Book"), #Displays book
    path("PCH/", views.care, name = "Care"), #displays care products
    path("Art/", views.arts, name="art"), #displays art section
    path('DSN/', views.DSN, name='dsn'), #Displays DSN
    path('Order/', views.order, name="order_success_ping"), #Displays success message
    path('Track_result/', views.track_result, name="track_result"), #Handles order tracker result
    path('Erono/', views.error_raise, name="error_page") #Raises error
]