from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
    ]
    context = {
        'title': 'sgmagar-crowdbotics-61',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
