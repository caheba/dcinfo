from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Change
# Create your views here.

#def index(request):
#    chg_list = Change.objects.order_by("-chg_number")[:3]
#    #chg_list = ["Carsten","Hugo","Martin"]
#    output = ", ".join([q.chg_title for q in chg_list])
#    return HttpResponse(output)
#    #return HttpResponse('Hier die Ausgabe von DCI')


def index(request):
    chg_list = Change.objects.order_by("-chg_number")[:5]
    template = loader.get_template("dci/index.html")
    context = {"chg_list": chg_list}
    return HttpResponse(template.render(context, request))
