from django.shortcuts import render
from .models import firstappVarity , Store
from django.shortcuts import get_object_or_404
from .forms import FirstAppForm
# Create your views here.
def all_firstapp(request):
    apps = firstappVarity.objects.all()
    return render(request, 'firstapp/all_firstapp.html', {"apps": apps})

def app_detail(request, app_id):
    app = get_object_or_404(firstappVarity, pk=app_id)
    return render(request, 'firstapp/app_details.html', {"app": app})

def app_store_views(request):
    stores =0
    if request.method == 'POST':
        form = FirstAppForm(request.POST)
        if form.is_valid():
            selected_app = form.cleaned_data['app_varity']
            stores = Store.objects.filter(app_varity=selected_app)
    else:
        form = FirstAppForm()
    return render(request, 'firstapp/app_Stores.html', {'form': form, 'stores': stores})