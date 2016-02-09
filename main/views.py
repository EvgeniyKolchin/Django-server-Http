from django.http import HttpResponseRedirect, Http404
from models import IBeacon
# Create your views here.

def get_image(request, major, minor):
	if IBeacon.objects.filter(minor=minor, major=major).exists():
		obj = IBeacon.objects.get(minor=minor, major=major)
		return HttpResponseRedirect(obj.image.url, status=301)
	raise Http404
