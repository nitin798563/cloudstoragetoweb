from django.shortcuts import render
from .models import Photo, Video

def home(request):
    photos = Photo.objects.all()
    videos = Video.objects.all()
    return render(request, 'home.html', {'photos': photos, 'videos': videos})






