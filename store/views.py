# Create your views here.
from django.http import HttpResponse

from store.models import ALBUMS


def index(request: object) -> HttpResponse:
    message = "StoreApp"
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)
