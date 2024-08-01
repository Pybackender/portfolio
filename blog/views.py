from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
from blog.forms import ContactForm
from blog.models import Post
from myservices.models import service
from Experience.models import EXPERIENCE
from myport.models import Port
from contact.models import Contact
from django.core.mail import send_mail

User = get_user_model()


def blogView(request):
    user = User.objects.get(id=1)
    myservices = service.objects.all()
    experiences = EXPERIENCE.objects.all()
    myport = Port.objects.all()
    contact = Contact.objects.all()
    blog = Post.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()  # This should work if the form is a ModelForm

            # Prepare email details
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            cc_myself = form.cleaned_data.get(
                "cc_myself", False)  # Ensure this field exists

            recipients = ["backender.py@gmail.com"]
            if cc_myself:
                recipients.append(email)
                

            send_mail(name, message, email, recipients)
            return HttpResponseRedirect("/")

    else:
        form = ContactForm()

    return render(request, 'landing/base.html', context={
        'user': user,
        'myservices': myservices,
        'experiences': experiences,
        'myport': myport,
        'contact': contact,
        'form': form,
        'blog': blog
    })
