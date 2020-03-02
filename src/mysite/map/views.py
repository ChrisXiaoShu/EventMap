from django.shortcuts import render
from django.template.loader import get_template
# Create your views here.
def map_index(request):
    """render map web index
    Augrment:
        request - http request
    Retrun:
        render index html
    """
    return render(request, './map_index.html')