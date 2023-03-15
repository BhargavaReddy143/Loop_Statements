from django.shortcuts import render

# Create your views here.
def loop(request):
    d={"name":"Bunny"}
    return render(request, 'one.html', d)