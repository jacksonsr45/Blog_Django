from django.shortcuts import render
from .models import User

def home(request):
    title = "Home"
    user = User.objects.get(id=1)

    return render( request, 'home.html', {'title': title,
                                        'user': user,})
