from django.shortcuts import render, redirect
from .forms import AddUploadForm
from .models import Shop, Brand
# Create your views here.


def index(request):
    mobiles = Shop.objects.all().order_by('-id')
    context = {'mobiles': mobiles}
    return render(request, 'accounts/index.html', context)


def add(request):
    if request.method == 'POST':
        form = AddUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return redirect('add')
    else:
        form = AddUploadForm()
        print("your data is not uploaded")
    context = {'form': form}
    return render(request, 'accounts/add.html', context)


