from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render (request, 'udomweb/homepage.html', {})
# =================staffpage section=============================
def staffpage(request):
    return render(request, 'udomweb/staffpage.html', {})
