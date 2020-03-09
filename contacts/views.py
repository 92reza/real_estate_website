from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from btre import config
# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for'+listing+'. Sign into the admin panel for more info',
            config.email_host_user,
            [realtor_email, 'reza.ghari@yahoo.com'],
            fail_silently=False
        )

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon!")
        return redirect('/listings/'+listing_id)