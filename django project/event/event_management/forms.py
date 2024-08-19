from django import forms
from .models import booking 


class DateInput(forms.DateInput):
    input_type='date'

    
class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'cus_name':'Customer Name',
            'cus_ph':'Phone Number'

        }
