from django.http import HttpRequest, HttpResponseRedirect


def home(request: HttpRequest):
    return HttpResponseRedirect('/shouldntwork')