__author__ = 'Csongor'

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
import string
import random
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


def home(request):
    return render(request, 'home.html', {})

def demos(request):
    return render(request, 'demos.html', {})


def youtubedemo(request):

    r = HttpResponse()
    if 'unique_id' in request.COOKIES:
        unique_id = request.COOKIES['unique_id']
    else:
        unique_id = generate_random_url()
        r.set_cookie("unique_id", unique_id)

    t = loader.get_template('youtube-demo.html')
    c = RequestContext(request, {"request": request, "unique_id": unique_id})

    r.content = t.render(c)
    return r


def youtuberemote(request, uniqueId):
    return render(request, 'youtube-remote.html', {})


def generate_random_url():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def shorturl(request, uniqueId):
    return render(request, 'youtube-remote.html', {})

@api_view(['POST'])
def registerurl(request):
    if request.method == 'POST':
        serializer = ShortenedUrlSerializer(data=request.DATA);
        if (serializer.is_valid()):
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return render(request, 'youtube-remote.html', {})