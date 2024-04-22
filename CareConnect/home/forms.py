from django import forms

from .models import Booking
from .models import ContactUs

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'p_name': "Patient Name",
            'p_phone': "Contact number",
            'p_email': "Patient email",
            'doc_name': "Doctor Name",
            'booking_date': "Booking Date",
         }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        labels = {
            'cont_name': "Contact Name",
            'cont_phone': "Contact number",
            'cont_email': "Email",
            'message': "Your message"
         }