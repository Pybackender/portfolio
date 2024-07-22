from django.shortcuts import render
# from account.models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from myservices.models import service


User = get_user_model()
services = get_user_model()


def blogView(request):
    user = User.objects.get(id=1)
    # list_users = User.objects.all()
    myservices = service.objects.all()

    context = {
        # 'list_users': list_users,
        'user': user,
        'myservices': myservices
    }
    return render(request, 'landing/base.html', context)
