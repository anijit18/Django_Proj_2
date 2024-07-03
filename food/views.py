from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    template=loader.get_template('food/index.html')
    item_list=Item.objects.all()
    context={
        'item_list': item_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    return render(request, 'food/detail.html', context)
    # return HttpResponse("This is the id %s" %item_id)
