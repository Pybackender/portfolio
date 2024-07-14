from django.shortcuts import render

# Create your views here.
def blogView(request):
    return render(request, 'base.html')