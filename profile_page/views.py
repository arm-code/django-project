from django.shortcuts import render

# Create your views here.


def alexis(request):
    return render(request, 'profile.html', {} )
