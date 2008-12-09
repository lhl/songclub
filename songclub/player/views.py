# Create your views here.

from django.contrib.auth.decorators import login_required
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from player.models import File

@login_required
def index(request):
  latest_folders = File.objects.filter(type='folder', mp3count__isnull=False).values('id', 'locationsha1', 'location', 'path', 'name', 'mtime')[:10]
  return render_to_response('index.html', {'latest_folders': latest_folders})

@login_required
def file(request, hash):
  f = File.objects.filter(locationsha1=hash).values('location', 'type', 'name', 'path', 'mimetype', 'mtime', 'size')[0]
  if f['type'] == 'folder':
    return HttpResponseNotFound("You tried to request a folder.")
    pass
  else:
    mimetype = 'audio/mpeg'

    response = HttpResponse(FileWrapper(open(f['location'])), content_type=mimetype)
    response['Content-Length'] = f['size']
    return response

    ''' Has to read the whole file...
    response = HttpResponse()
    response['Content-Type'] = mimetype
    response['Content-Length'] = f['size']
    response.content = open(f['location']).read()
    return response
    '''


"""
    files = File.objects.filter(path=f['location'][:-1]).values('location', 'type', 'name', 'path', 'mimetype', 'mtime')
    for f in files:
      print f
    return HttpResponse("Hello, world. You're looking for a file: %s" % f['location'])
  else:
"""
