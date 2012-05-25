from django.http import render_to_response, get_object_or_404
from django.template import Context, loader
from music.freeplay.models import File

def index(request):
  filelist = File.objects.all().order_by('-updated')[:5]
  return render_to_response('index.html', {'filelist': filelist})


def detail(request, file_id):
  f = get_object_or_404(File, pk=file_id)
  return render_to_response('detail.html', {'file': f})
