from django.shortcuts import render

from .models import Donation
from .forms import DonationForm

import razorpay


client = razorpay.Client(auth=("rzp_test_9GtISjPbi1bNeB", "TXyNCg77zThOEcQ8g9p5tQDl"))

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            print(donation.id,donation.name,str(donation.amount))
            data = {
                'amount':donation.amount * 100,
                'currency': 'INR',
                'receipt': str(donation.id),
                'payment_capture':'0',
                'notes': {
                    'name': donation.name
                }
            }
            resp = client.order.create(data=data)
            donation.payment_id = resp['id']
            donation.save()

            context = {
                'id': resp['id'],
                'amount': resp['amount'] * 100,
                'name': donation.name
            }
            return render(request,'checkout.html',context=context)
    return render(request,'home.html')

def success(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        donation = Donation.objects.get(payment_id=data['razorpay_order_id'])
        donation.payment_captured = True
        donation.save()
        return render(request,'success.html',context={"name":donation.name})

