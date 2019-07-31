from django.shortcuts import render
from photogur.models import Picture

def pictures(request):
    pictures = Picture.objects.all()
    context = {"pictures": pictures}
    return render(request, 'pictures.html', context)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}
    return render(request, 'picture.html', context)