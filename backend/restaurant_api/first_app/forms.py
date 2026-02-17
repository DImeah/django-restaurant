from django import forms

from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields ='__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'style':'width:100%;padding:10px;margin:6px 0 14px;border-radius:6px;border:1px solid #ccc;'}),
            'last_name': forms.TextInput(attrs={'style':'width:100%;padding:10px;margin:6px 0 14px;border-radius:6px;border:1px solid #ccc;'}),
            'guest_count': forms.NumberInput(attrs={'style':'width:100%;padding:10px;margin:6px 0 14px;border-radius:6px;border:1px solid #ccc;'}),
            'comments': forms.Textarea(attrs={'style':'width:100%;padding:10px;margin:6px 0 14px;border-radius:6px;border:1px solid #ccc;'}),
        }
