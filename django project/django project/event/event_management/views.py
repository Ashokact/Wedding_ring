from django.shortcuts import render , redirect , get_object_or_404
from . models import event , booking
from . forms import BookingForm
from django.contrib.auth.decorators import login_required

def home(request):
    dict_eve={
        'eve':event.objects.all()
    }
    return render(request,'home.html',dict_eve)


def Eventlisting(request):
    dict_eve={
        'eve':event.objects.all()
    }
    return render(request,'Eventlisting.html',dict_eve)


def Eventdetail(request):
    return render(request,'Eventdetail.html')


login_required
def Profilemanagement(request):
    return render(request,'Profilemanagement.html')


def bookingsystem(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookingForm()

    booking_count = booking.objects.count()
    context = {
        'form': form,
        'booking_count': booking_count
    }
    return render(request, 'bookingsystem.html', context)


def booking_list(request):
    bookings = booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})


def crew_home(request):
    if request.user.is_authenticated and request.user.is_staff:
        booking_count = booking.objects.count()
        bookings = booking.objects.all()
        context = {
            'booking_count': booking_count,
            'bookings': bookings
        }
        return render(request, 'crew/crew_home.html', context)
    else:
        return render(request, 'crew/crew_home.html')
