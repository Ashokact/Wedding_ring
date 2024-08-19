from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('Eventlisting/',views.Eventlisting ,name='eventlist'),
    path('Eventdetail/',views.Eventdetail,name='eventdetails'),
    path('Profilemanagement/',views.Profilemanagement,name='manager'),
    path('Bookingsystem/',views.bookingsystem,name='bookingsystem'),
    path('booking_list/', views.booking_list, name='booking_list'),

    # crewkhkjhjkhkkjgjdd

    path('crew_home',views.crew_home, name='crew_home'),
]