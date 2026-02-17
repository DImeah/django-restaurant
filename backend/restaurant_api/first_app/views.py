from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")


class HelloEthopia(View):
    def get(self, request):
        return HttpResponse("HelloEthopia")
    
def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            # return HttpResponse("Success")
            messages.success(request, "Reservation booked successfully!")
            return redirect('success')
        
        else:
            form = ReservationForm()
        
    return render(request, 'index.html', {'form': form})


def success(request):
    return render(request, 'success.html')

