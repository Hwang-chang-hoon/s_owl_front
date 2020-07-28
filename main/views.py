from django.shortcuts import render
from point.views import throw_point

def main(request):
    mypoint = throw_point(request)
    return render(request, 'main/main.html', {'mypoint': mypoint})
