from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def website_login(request):
    return render_to_response('index.html',locals())

