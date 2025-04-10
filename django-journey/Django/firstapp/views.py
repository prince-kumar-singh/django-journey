from django.shortcuts import render
from .models import firstappVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_firstapp(request):
    apps = firstappVarity.objects.all()
    return render(request, 'firstapp/all_firstapp.html', {"apps": apps})

def app_detail(request, app_id):
    app = get_object_or_404(firstappVarity, pk=app_id)
    return render(request, 'firstapp/app_details.html', {"app": app})