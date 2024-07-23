from django.shortcuts import render
# from account.models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from myservices.models import service
from Experience.models import EXPERIENCE
from myport.models import Port

User = get_user_model()
services = get_user_model()


def blogView(request):
    user = User.objects.get(id=1)
    myservices = service.objects.all()
    experiences = EXPERIENCE.objects.all()
    myport = Port.objects.all()

    context = {
        'user': user,
        'myservices': myservices,
        'experiences': experiences,
        'myport':myport
    }
    return render(request, 'landing/base.html', context)
