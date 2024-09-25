from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"].title()
            last_name = form.cleaned_data["last_name"].title()
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"].title()

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            
            message_body = f"Thank you, {first_name}. Your job application was submitted."\
                           f"\n\nHere is the information you provided:\n"\
                           f"Last Name: {last_name}\n"\
                           f"First Name: {first_name}\n"\
                           f"Email Address: {email}\n"\
                           f"Date Available: {date}\n"\
                           f"Current Occupation: {occupation}\n\n"\
                           f"You will hear from us soon regarding your application status. Thanks again!"

            email_message = EmailMessage("Form Submission Confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submmitted successfully!")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def job_postings(request):
    return render(request, "job_postings.html")
