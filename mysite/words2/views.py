from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):

    return render(request=request,
                  template_name="words2/index.html")