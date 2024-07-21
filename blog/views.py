from django.shortcuts import render
# from account.models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from myservices.models import service


User = get_user_model()
services = get_user_model()


def blogView(request):
    users = User.objects.get(id=1)
    myservices = service.objects.all()
    print(myservices,111111111111111111111111)
    context = {
        users:"users",
        myservices:"myservises"
    }
    return render(request, 'landing/base.html', context)
