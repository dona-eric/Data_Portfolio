from django.shortcuts import render, redirect
from . models import Photo
from . forms import PhotoForm




def photo_upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user

            photo.save()
            return redirect('home_photo')
        
    else:
        form = PhotoForm()
    return render(request, 'photo/photo.html', context={'form': form})



# vue pour home pour afficher toutes les photos

def home_photo(request):
    photos = Photo.objects.all()
    return render(request, 'photo/home.html', context={'photos': photos})