from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Service
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.http import HttpResponseBadRequest

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show_detail(request):
    services = Service.objects.all()
    return render(request, 'show_detail.html', {'services': services})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, "Service record deleted successfully.")
    return redirect('show_detail')

def update_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        service.name = request.POST.get('name')
        service.email = request.POST.get('email')
        service.phone = request.POST.get('phone')
        if request.FILES.get('file'):
            service.file = request.FILES.get('file')
        service.save()
        messages.success(request, "Service record updated successfully.")
        return redirect('show_detail')
    return render(request, 'show_detail.html', {'service': service})

def add_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.FILES.get('file')
        service_instance = Service(name=name, email=email, phone=phone, file=file)
        service_instance.save()
        messages.success(request, "Added new service successfully.")
        return redirect('show_detail') 
    return render(request, 'show_detail.html')

def service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.FILES.get('file')
        service_instance = Service(name=name, email=email, phone=phone, file=file)
        service_instance.save()
        messages.success(request, "Your Data has been sent successfully.")
    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # Create object of Contact
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        try:
            send_mail(
                subject="New Contact Form Submission",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nDescription: {desc}",
                from_email="nasreenshah704@gmail.com",
                recipient_list=["nasreen.shah@isk.studio"],
            )
            contact.save()
            messages.success(request, "Your data is sent successfully.")
        except BadHeaderError:
            return HttpResponseBadRequest('Invalid header found.')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'contact.html')