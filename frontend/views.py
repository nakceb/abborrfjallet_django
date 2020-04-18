
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render


def main(request, *ars, **kwargs):
    try:
        return render(request, "frontend/base.html", {})
    except Exception as ex:
        return HttpResponseBadRequest(str(ex))
