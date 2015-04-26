from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from .models import Audio


# Create your views here.
def index(request):
    latest_question_list = Audio.objects.order_by('-pub_date')[:5]
    template = loader.get_template('kichiku/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))