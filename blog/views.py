from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from blog.forms import ContactForm
from blog.models import Post, Tag
from myservices.models import service
from Experience.models import EXPERIENCE
from myport.models import Port
from contact.models import Contact
from django.core.mail import send_mail
from django.contrib import messages

User = get_user_model()

def blogView(request):
    user = get_object_or_404(User, id=1)
    myservices = service.objects.all()
    experiences = EXPERIENCE.objects.all()
    myport = Port.objects.all()
    contact = Contact.objects.all()
    blog = Post.objects.prefetch_related("tags").all()
    
    # list_ip =[]
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    # list_ip.append(ip)
    for i in blog:
        
        # if ip in list_ip:
            # i.viewers += 0
        # else:
            i.viewers += 1
    

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            # form.save()  # This should work if the form is a ModelForm

            
            form.save(commit=False)
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            mobile_number = form.cleaned_data["mobile_number"]
            # cc_myself = form.cleaned_data.get("cc_myself", False)
            recipients = ["backender.py@gmail.com"]
            # if cc_myself:
            # recipients.append(email)

            try:
                send_mail(
                    subject=name,  # Subject can be the name or a custom subject
                    message=f"Message: {message}\nMobile: {mobile_number}\nFrom: {email}",
                    from_email=email,
                    recipient_list=recipients,
                )
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

            
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect("/#contact")

    else:
        form = ContactForm()

    return render(request, 'landing/base.html', context={
        'user': user,
        'myservices': myservices,
        'experiences': experiences,
        'myport': myport,
        'contact': contact,
        'form': form,
        'blog': blog,
    })
