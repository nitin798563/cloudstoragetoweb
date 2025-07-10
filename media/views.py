from django.shortcuts import render
from .models import Photo, Video
from django.core.management import call_command
from django.http import HttpResponse

def home(request):
    photos = Photo.objects.all()
    videos = Video.objects.all()
    return render(request, 'home.html', {'photos': photos, 'videos': videos})



def create_admin_on_render(request):
    try:
        call_command('loaddata', 'superuser.json')
        return HttpResponse("✅ Superuser created successfully!")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

def migrate_view(request):
    try:
        call_command('makemigrations')
        call_command('migrate')
        return HttpResponse("✅ Migration done successfully!")
    except Exception as e:
        return HttpResponse(f"❌ Migration error: {e}")



