from django.shortcuts import render

from .forms import DonationForm

import razorpay


client = razorpay.Client(auth=("rzp_test_9GtISjPbi1bNeB", "TXyNCg77zThOEcQ8g9p5tQDl"))

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'checkout.html')
    return render(request,'home.html')

